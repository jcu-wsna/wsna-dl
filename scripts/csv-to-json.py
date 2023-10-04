#!/usr/bin/env python3
""" csv-to-json

    This reads the library-index.csv spreadsheet and generates a
    library-index.json file from the information in the spreadsheet.

    The paths and names of files are all defined in constants at
    the top of the file, as are the column names for the csv file.

    The script requires the structlog library to be installed
    (used for logging).
"""

import json
import os
from pathlib import Path
import csv
import structlog
import argparse

# paths and filenames
LIBRARY_INDEX_FILE = Path("./data/library-index.csv").resolve()
LIBRARY_DOCS_PATH = Path("../src/statics/data/").resolve()
JSON_PATH = Path("../src/statics/").resolve()
JSON_FILENAME = "library-index.json"
DOWNLOAD_PATH = "/statics/data/"

# library-index.csv column names used in processing
#
ID = "ID"
ACCESS = "Access_Rights"
FILE_NAME = "File_name"
PUBLISHED_URL = "URL"
STATUS = "Status"

# items added when generating library-index.json
DISPLAY_URL = "URL"
DISPLAY_ICON = "icon"

# Column values used in script
ACCESS_OPEN = "free to download"
ACCESS_JCU_LIBRARY = "request from jcu library"
ACCESS_PUBLISHER = "download from publisher"

# URLs added for certain circumstances
JCU_LIBRARY_URL = "https://www.jcu.edu.au/library"
CONTACT_SUPPORT_URL = "/contact-us"

# icons to display for documents
ICON_OPEN_WEBPAGE = "open_in_new"
ICON_DOWNLOAD = "file_download"
ICON_SUPPORT = "contact_support"
ICON_LIBRARY = "local_library"

# columns that can contain multiple comma separated tokens
MULTI_OPTION_COLS = ["Catchment", "State", "Habitat_type"]

final_json = []
is_dry_run = False


def split_multi_option_values(data):
    # data is a list of dictionary items
    #
    # Work through the list and for each dictionary item:
    #   For the keys in MULTI_OPTION_COLS, the value of the item for that key is
    #   a string containing 1 or more tokens separated by commas.
    #   Extract the tokens and replace the value with an array of strings
    #   where each string is a token.
    #
    for item in data:
        for key in MULTI_OPTION_COLS:
            if key in item.keys():
                item[key] = [elem.strip() for elem in item[key].split(",")]

    return data


def normalise_file_name(filename):
    return filename.replace(" ", "_").replace("/", "_")


def set_url_to_JCUlibrary(log, file_info):
    file_info[DISPLAY_URL] = JCU_LIBRARY_URL
    file_info[DISPLAY_ICON] = ICON_LIBRARY
    return file_info


def set_url_to_contact_support(log, file_info):
    file_info[DISPLAY_URL] = CONTACT_SUPPORT_URL
    file_info[DISPLAY_ICON] = ICON_SUPPORT
    return file_info


def set_url_to_external_site(log, file_info):
    if file_info[PUBLISHED_URL] == "":
        log.error(
            "ID {} | {} is {} and {} is empty.".format(
                file_info[ID], ACCESS, ACCESS_PUBLISHER, PUBLISHED_URL
            )
        )
        return None

    file_info[DISPLAY_URL] = file_info[PUBLISHED_URL]
    file_info[DISPLAY_ICON] = ICON_OPEN_WEBPAGE
    return file_info


def set_url_to_download_file(log, file_info, os):
    """Check a file exists and normalise its name if necessary.

    This function should only be called if ACCESS value == ACCESS_OPEN,
    so there should be a file for the document.

    Log warnings if there is no file name in the file_info or if the file doesn't exist.
    """

    # Extract existing name and generate web friendly name (normalise)
    original_pdf_name = file_info[FILE_NAME]
    normalised_pdf_file_name = normalise_file_name(original_pdf_name)

    if original_pdf_name == "":
        # This file doesn't have a PDF file name in the csv file
        log.error(
            "ID {} | {} document has no {} value in spreadsheet. ".format(
                file_info[ID], ACCESS_OPEN, FILE_NAME
            )
        )

        return None

    # If the original file name from the csv was normalised,
    # we need to rename the file to match
    if os.path.isfile(original_pdf_name) and not os.path.isfile(
        normalised_pdf_file_name
    ):
        try:
            if not is_dry_run:
                os.rename(original_pdf_name, normalised_pdf_file_name)

            log.info(
                "ID {} | Renamed {} to {}.".format(
                    original_pdf_name, normalised_pdf_file_name
                )
            )
        except Exception as ex:
            log.exception(
                "ID {} | Rename of {} failed.".format(
                    file_info["ID"], original_pdf_name
                )
            )
            return None

    if is_dry_run:
        if not (
            os.path.isfile(original_pdf_name)
            or os.path.isfile(normalised_pdf_file_name)
        ):
            log.error(
                "ID {} | Open access document does not exist.".format(file_info[ID])
            )
            return None
        else:
            log.info(
                "ID {} | Document exists and will be added to JSON file".format(
                    file_info[ID]
                )
            )

        return file_info

    # Check if a file with the normalised name exists before setting url to the
    # normalised file name
    if os.path.isfile(normalised_pdf_file_name):
        # the download url is served from a different base directory
        # hence the different path
        file_info[DISPLAY_URL] = "{}{}".format(DOWNLOAD_PATH, normalised_pdf_file_name)

        log.info(
            "ID {} | Setting {} to {}".format(
                file_info[ID], DISPLAY_URL, file_info[DISPLAY_URL]
            )
        )
    else:
        log.error(
            "ID {} | {} document does not exist.".format(file_info[ID], ACCESS_OPEN)
        )
        return None

    file_info[DISPLAY_ICON] = ICON_DOWNLOAD
    return file_info


if __name__ == "__main__":
    log = structlog.get_logger()

    # create parser
    parser = argparse.ArgumentParser()

    # add arguments to the parser
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="don't make any changes but give me some stats on what would happen",
    )

    # parse the command line arguments
    args = parser.parse_args()
    is_dry_run = args.dry_run
    if is_dry_run:
        log.info("This is a dry-run, no changes will be made")

    # log some useful information
    log.info("Creating/renaming files in {}".format(LIBRARY_DOCS_PATH))
    log.info("Loading csv file from {}".format(LIBRARY_INDEX_FILE))

    with open(LIBRARY_INDEX_FILE, encoding="utf-8") as fd:
        # change cwd to the directory which contains data files
        os.chdir(LIBRARY_DOCS_PATH)

        for row in csv.DictReader(fd):
            file_info = None
            print("type(row) (", type(row))  # DEBUG

            # strip any trailing whitespace from each row value
            for key, value in row.items():
                row[key] = value.strip()

            # setting the URL based on the ACCESS value for the document
            if ACCESS_JCU_LIBRARY == row[ACCESS].lower():
                file_info = set_url_to_JCUlibrary(log, row)
            elif ACCESS_OPEN == row[ACCESS].lower():
                file_info = set_url_to_download_file(log, row, os)
            elif ACCESS_PUBLISHER == row[ACCESS].lower():
                file_info = set_url_to_external_site(log, row)
            else:
                log.error(
                    "ID {} | Invalid {} field value '{}'".format(
                        row[ID], ACCESS, row[ACCESS]
                    )
                )

            if file_info is not None:
                final_json.append(file_info)

    # convert the list of dictionary items to json string format
    output = json.dumps(split_multi_option_values(final_json))

    # write to file
    os.chdir(JSON_PATH)

    json_array_output_file = open(JSON_FILENAME, "w")
    json_array_output_file.write(output)

    log.info(
        "Wrote JSON file, {}, to {}. Exiting.".format(json_array_output_file, JSON_PATH)
    )
