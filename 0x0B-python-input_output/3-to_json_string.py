#!/usr/bin/python3
"""defines a function to_json_string()"""


import json

def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)

    args:
        my_obj: object to return as JSON
    """

    return json.dumps(my_obj)
