#!/usr/bin/python3
"""defines a function to_json_string()"""

import json


def to_json_string(my_obj):
    """Convert a Python object to a JSON string.

    Args:
        my_obj: The Python object to be converted to JSON.

    Returns:
        str: The JSON string representation of the Python object.
    """

    return json.dumps(my_obj)
