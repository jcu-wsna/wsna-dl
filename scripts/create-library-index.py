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
import re
import structlog
import argparse
import libhelper
from confighelper import (
    docs,
    label,
    access_types,
    status_types,
    icons,
    urls,
    files,
)

# columns that can contain multiple comma separated tokens
# TODO - move into a new row in the spreadsheet like the search and filter flags
MULTI_OPTION_COLS = ["Catchment", "State", "Habitat_type", "Region"]

is_dry_run = False


def split_multi_option_values(lib_data):
    # Split the multi-option columns in to lists of strings
    # hopefully this won't break the lib_docs.to_json function

    #   For the keys in MULTI_OPTION_COLS, the value of the item for that key is
    #   a string containing 1 or more tokens separated by commas.
    #   Extract the tokens and replace the value with an array of strings
    #   where each string is a token.
    #
    for column in MULTI_OPTION_COLS:
        log.debug("split_multi_option_values: splitting {}".format(column))
        lib_data[column] = (
            lib_data[column]
            .str.split(",")
            .apply(lambda x: [item.strip() for item in x])
        )
        log.debug("split_multi_option_values: lib_data[{}]\n".format(lib_data[column]))

    return lib_data


def create_library_index(log, is_dry_run, lib_data):
    # log some useful information
    log.info("Creating library_index for website, {}".format(files.libindex_json))

    # set label.url value for access via a physical library
    lib_data.loc[
        lib_data[label.access] == access_types.physical_library, label.displayURL
    ] = urls.physical_library
    lib_data.loc[
        lib_data[label.access] == access_types.physical_library, label.displayIcon
    ] = icons.library

    # set label.url value for open access documents (can download directly from the library)
    lib_data.loc[lib_data[label.access] == access_types.open, label.displayURL] = (
        urls.download + lib_data[label.filename]
    )
    lib_data.loc[
        lib_data[label.access] == access_types.open, label.displayIcon
    ] = icons.download

    # set label.url value for documenets accessed from an external website
    lib_data.loc[
        lib_data[label.access] == access_types.publisher, label.displayURL
    ] = lib_data[label.publishedURL]
    lib_data.loc[
        lib_data[label.access] == access_types.publisher, label.displayIcon
    ] = icons.webpage

    # convert the list of dictionary items to json string format
    json_lib_data = lib_data.to_json(orient="records")

    if not is_dry_run:
        # write to file
        json_array_output_file = files.libindex_json.open(mode="w", encoding="utf-8")
        json_array_output_file.write(json_lib_data)

        log.info("Wrote JSON file to {}".format(files.libindex_json))

    return lib_data


def get_searchable_fields(log):
    data = pd.read_csv(files.search_config, index_col=label.id)
    search_fields = data.columns[data.iloc[0]].to_list()
    log.info("The searchable fields for libary are: {}".format(search_fields))
    return search_fields


def get_filter_list(log):
    data = pd.read_csv(files.filter_config, index_col=label.id)
    filter_items = data.columns[data.iloc[0]].to_list()
    log.info("The filter fields for libary are: {}".format(filter_items))
    return filter_items


def remove_private_details(log, lib_data):
    # Read in the appropriate config file and drop any columns
    # from lib_data that are set to False in the config file

    public_labels = pd.read_csv(files.doc_display_config, index_col=label.id)
    col_list = public_labels.columns[~public_labels.iloc[0]].to_list()
    lib_data = lib_data.drop(columns=col_list)
    log.info("Dropped {} columns".format(col_list))

    return lib_data


def remove_invalid_access_rows(log, lib_data):
    # Get a list of docs with an invalid access type
    problem_docs = lib_data[
        ~lib_data[label.access].isin(access_types._asdict().values())
    ]
    # log a warning message for these problem docs
    for index, row in problem_docs.iterrows():
        log.warning(
            "ID {} | Invalid access value, {} ".format(index, row[label.access])
        )

    # log.debug("remove_invalid_access_rows: problem_docs\n{}".format(problem_docs))

    # Drop any docs with invalid access values
    lib_data = lib_data.drop(index=problem_docs.index.to_list())
    return lib_data


def remove_openaccess_nofilename_rows(log, lib_data):
    # Remove all rows where access is open and filename is empty

    # Get the list of files for the library.
    doc_list = os.listdir(docs.dest_path)

    # Get a list of the open access docs that don't have a file in the library
    problem_docs = lib_data[
        (lib_data[label.access] == access_types.open)
        & (~lib_data[label.filename].isin(doc_list))
    ]
    # log a warning message for these problem docs
    for index, doc in problem_docs.iterrows():
        log.warning(
            "ID {} | {} access document file is missing, {}".format(
                index, access_types.open, doc[label.filename]
            )
        )

    # Drop any open access documents that we don't have a copy of the document for
    lib_data = lib_data.drop(index=problem_docs.index.to_list())
    return lib_data


def remove_publisheraccess_nourl_rows(log, lib_data):
    # Get a list of the external access docs that don't have a URL in the lib data
    problem_docs = lib_data[
        (lib_data[label.access] == access_types.publisher)
        & (lib_data[label.publishedURL] == "")
    ]
    # log a warning message for these problem docs
    for index, doc in problem_docs.iterrows():
        log.warning(
            "ID {} | Doc with {} access {} value is empty".format(
                index, access_types.publisher, label.publishedURL
            )
        )

    # Drop any open access documents that we don't have a copy of the document for
    lib_data = lib_data.drop(index=problem_docs.index.to_list())
    return lib_data


def remove_nonactive_rows(log, lib_data):
    # Drop all rows that don't have status set to Active
    # unless there is no Status column
    if label.status in lib_data.columns:
        lib_data = lib_data[lib_data.Status == status_types.active]
        log.info("Extracted only the {} records to process".format(status_types.active))

    return lib_data


def create_query_config(log, lib_data, search_fields, filter_fields):
    # TODO Sorting config is still hard-coded, need to fix this at some point
    log.debug("about to start create_query_config function")

    # build aggregations structure as a Dictionary
    filters = {}
    for field in filter_fields:
        field_id = re.sub(
            r"[^A-Za-z0-9]", "_", field
        )  # replace spaces etc with underscores

        if field in MULTI_OPTION_COLS:
            unique_filters = set(x for sublist in lib_data[field] for x in sublist)
        else:
            unique_filters = lib_data[field].unique().tolist()

        log.debug(
            "create_query_string: field {}, field_id {}, unique_filters: {}".format(
                field, field_id, unique_filters
            )
        )
        filters[field_id] = {"title": field, "size": len(unique_filters)}

    query_config = {
        "sortings": {
            "name_asc": {
                "field": "Title",
                "order": "asc",
            },
            "year_name_asc": {
                "field": ["Year", "Title"],
                "order": ["desc", "asc"],
            },
        },
        "searchableFields": search_fields,
        "aggregations": filters,
    }

    log.debug("create_query_config: query_config({})".format(query_config))

    # Create/overwrite query_config json file
    # See confighelper.py for file names
    config_file = files.query_config.write_text(
        json.dumps(query_config), encoding="utf-8"
    )

    log.info("Query config into written to {}".format(files.query_config))


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

    log.info("Loading csv file from {}".format(files.libindex_csv))

    # Read in data from the library-index.csv file and ensure that
    # there are no leading or trailing spaces on the contents
    lib_data = pd.read_csv(files.libindex_csv, index_col=label.id, dtype="str")
    lib_data = lib_data.map(lambda x: x.strip() if type(x) == str else x)

    lib_data = remove_nonactive_rows(log, lib_data)
    lib_data = remove_invalid_access_rows(log, lib_data)
    lib_data = remove_openaccess_nofilename_rows(log, lib_data)
    lib_data = remove_publisheraccess_nourl_rows(log, lib_data)
    # must call remove_nonactive_rows last in case it removes a
    # column needed for other processing
    lib_data = remove_private_details(log, lib_data)
    lib_data = split_multi_option_values(lib_data)

    lib_data = create_library_index(log, is_dry_run, lib_data)
    create_query_config(log, lib_data, get_searchable_fields(log), get_filter_list(log))

    log.info("library index and query config file creation is complete")
