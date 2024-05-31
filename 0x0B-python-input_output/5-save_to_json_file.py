#!/usr/bin/python3
"""
    defines a function save_to_json_file()
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    args:
        my_obj: The object to be written to the file
    """

    json.dump(my_obj, filename)
