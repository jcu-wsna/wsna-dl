#!/usr/bin/env python3
""" create-library-index.py

    This reads the library-index spreadsheet and generates a
    library-index.json file from the information in the spreadsheet.

    The paths and names of files are all defined in constants at
    the top of the file, as are the column names for the csv file.

    The script requires the structlog library to be installed
    (used for logging).
"""
import pandas as pd
import json
import os
import csv
import structlog
import argparse
from confighelper import docs, label, access_types, icons, libindex, urls

DOC_DETAILS_CONFIG = "outputs/doc-display-config.csv"

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
    file_info[label.displayURL] = urls.physical_library
    file_info[label.displayIcon] = icons.library
    return file_info


def set_url_to_contact_support(log, file_info):
    file_info[label.displayURL] = urls.contact_us
    file_info[label.displayIcon] = icons.support
    return file_info


def set_url_to_external_site(log, file_info):
    if file_info[label.publishedURL] == "":
        log.error(
            "ID {} | {} is {} and {} is empty.".format(
                file_info[label.id],
                label.access,
                access_types.publisher,
                label.publishedURL,
            )
        )
        return None

    file_info[label.displayURL] = file_info[label.publishedURL]
    file_info[label.displayIcon] = icons.webpage
    return file_info


def set_url_to_download_file(log, file_info, os):
    """Check a file exists and normalise its name if necessary.

    This function should only be called if ACCESS value == ACCESS_OPEN,
    so there should be a file for the document.

    Log warnings if there is no file name in the file_info or if the file doesn't exist.
    """

    # Extract existing name and generate web friendly name (normalise)
    original_filename = file_info[label.filename]
    normalised_filename = normalise_file_name(original_filename)

    if original_filename == "":
        # This file doesn't have a PDF file name in the csv file
        log.error(
            "ID {} | {} document has no {} value in spreadsheet. ".format(
                file_info[label.id], access_types.open, label.filename
            )
        )

        return None

    # If the original file name from the csv was normalised,
    # we need to rename the file to match
    if (original_filename != normalised_filename) and os.path.isfile(original_filename):
        try:
            if not is_dry_run:
                os.rename(original_filename, normalised_filename)

            log.info(
                "ID {} | Renamed {} to {}.".format(
                    original_filename, normalised_filename
                )
            )
        except Exception as ex:
            log.exception(
                "ID {} | Rename of {} failed.".format(
                    file_info[label.id], original_filename
                )
            )
            return None

    if is_dry_run:
        if not (
            os.path.isfile(original_filename) or os.path.isfile(normalised_filename)
        ):
            log.error(
                "ID {} | {} document does not exist.".format(
                    file_info[label.id], access_types.open
                )
            )
            return None
        else:
            log.info(
                "ID {} | Document exists and will be added to JSON file".format(
                    file_info[label.id]
                )
            )

        return file_info

    # Check if a file with the normalised name exists before setting url to the
    # normalised file name
    if os.path.isfile(normalised_filename):
        # the download url is served from a different base directory
        # hence the different path
        file_info[label.displayURL] = "{}{}".format(docs.urlPath, normalised_filename)

        log.info(
            "ID {} | Setting {} to {}".format(
                file_info[label.id], label.displayURL, file_info[label.displayURL]
            )
        )
    else:
        log.error(
            "ID {} | {} document, {}, does not exist.".format(
                file_info[label.id], access_types.open, normalised_filename
            )
        )
        return None

    file_info[label.displayIcon] = icons.download
    return file_info


def create_library_index(log, is_dry_run, visible_details):
    # log some useful information
    log.info("Creating/renaming files in {}".format(docs.dest_path))
    log.info("Loading csv file from {}".format(libindex.csv))

    with libindex.csv.open(mode="r", encoding="utf-8") as fd:
        # change cwd to the directory which contains data files
        os.chdir(docs.dest_path)

        for row in csv.DictReader(fd):
            file_info = None

            # strip any trailing whitespace from each row value
            for key, value in row.items():
                row[key] = value.strip()

            # setting the URL based on the ACCESS value for the document
            if access_types.physical_library == row[label.access].lower():
                file_info = set_url_to_JCUlibrary(log, row)
            elif access_types.open == row[label.access].lower():
                file_info = set_url_to_download_file(log, row, os)
            elif access_types.publisher == row[label.access].lower():
                file_info = set_url_to_external_site(log, row)
            else:
                log.error(
                    "ID {} | Invalid {} field value '{}'".format(
                        row[label.id], label.access, row[label.access]
                    )
                )

            if file_info is not None:
                final_json.append(file_info)

    # convert the list of dictionary items to json string format
    output = json.dumps(split_multi_option_values(final_json))

    # write to file
    json_array_output_file = libindex.json.open(mode="w", encoding="utf-8")
    json_array_output_file.write(output)

    log.info("Wrote JSON file to {}".format(libindex.json))


def create_search_config(log, is_dry_run):
    return


def create_filter_config(log, is_dry_run):
    #
    return


def remove_private_details(log, lib_data):
    # Read in the appropriate config file and drop any columns
    # from lib_data that are set to False in the config file

    public_labels = pd.read_csv(DOC_DETAILS_CONFIG)
    lib_data = lib_data.drop(columns=public_labels.index[public_labels].to_list())
    log.info("Dropped all unnecessary columns as listed in {}", DOC_DETAILS_CONFIG)

    return lib_data


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

    lib_data = pd.read_csv(libindex.csv_filename, index_col=label.id)
    lib_data = remove_private_details(log, lib_data)  # TODO - test
    create_library_index(log, is_dry_run, lib_data)
    create_search_config(log, is_dry_run)  # TODO - write
    create_filter_config(log, is_dry_run)  # TODO - write
    log.info("create-library-index creation is complete")
