#!/usr/bin/python3
"""defines a function load_from_json_file()"""

import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file """

    with open(filename, encoding="utf-8") as lfile:
        lfile.read()
        return load(lfile)
