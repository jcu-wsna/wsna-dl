# config.py
#
# This file contains the configurable items for specific
# digital library source data.
#

import configparser
from collections import namedtuple
from pathlib import Path

config = {}


def load_config():
    config = configparser.ConfigParser()
    config.read("library-config.ini")
    return config


def get_docs_config(config):
    docs_config = namedtuple("Docs", ["file_pattern", "src_path", "dest_path"])
    return docs_config(
        file_pattern=config["Library-docs"]["filePattern"],
        src_path=Path(config["Library-docs"]["srcPath"]).resolve(),
        dest_path=Path(config["Library-docs"]["destPath"]),
    )


def get_libindex_config(config):
    libindex_config = namedtuple("LibIndex", ["csv_filename", "json_filename"])
    return libindex_config(
        csv_filename=Path(config["Library-index"]["libraryIndexCSV"]).resolve(),
        json_filename=Path(config["Library-index"]["libraryIndexJSON"]).resolve(),
    )


def get_label_config(config):
    label_config = namedtuple(
        "Labels", ["id", "access", "filename", "publishedURL", "status"]
    )
    return label_config(
        id=config["Column-labels"]["id"],
        access=config["Column-labels"]["access"],
        filename=config["Column-labels"]["filename"],
        publishedURL=config["Column-labels"]["publishedURL"],
        status=config["Column-labels"]["status"],
    )


def get_access_values(config):
    access_config = namedtuple(
        "AccessValues", ["open", "physical_library", "publisher"]
    )
    return access_config(
        open=config["Access-values"]["open"],
        physical_library=config["Access-values"]["physicalLibrary"],
        publisher=config["Access-values"]["publisher"],
    )


def get_status_values(config):
    status_values = namedtuple("StatusValues", ["active", "deleted"])
    return status_values(
        active=config["Status-values"]["active"],
        deleted=config["Status-values"]["deleted"],
    )


def get_icons(config):
    icons = namedtuple("Icons", ["webpage", "download", "support", "library"])
    return icons(
        webpage=config["Icons"]["webpage"],
        download=config["Icons"]["download"],
        support=config["Icons"]["support"],
        library=config["Icons"]["library"],
    )


def get_urls(config):
    urls = namedtuple("URLs", ["physical_library", "contact_us"])
    return urls(
        physical_library=config["URLs"]["physicalLibrary"],
        contact_us=config["URLs"]["contactUs"],
    )


# load config info for use
config = load_config()
docs = get_docs_config(config)
libindex = get_libindex_config(config)
label = get_label_config(config)
access_types = get_access_values(config)
status_types = get_status_values(config)
icons = get_icons(config)
urls = get_urls(config)
