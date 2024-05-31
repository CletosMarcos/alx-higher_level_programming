#!/usr/bin/python3
"""
    This module provides a function to convert a JSON string
    to a Python object.

    the function:
    - from_json_string(my_str): Converts the given JSON string
    to a Python object.
"""

import json


def from_json_string(my_str):
    """Convert a JSON string to a Python object.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python object representation of the JSON string.
    """

    return json.load(my_str)
