#!/usr/bin/python3

"""Module that defines a function class_to_json()
    that serializes a class to json
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    args:
        obj:  is an instance of a Class

    All attributes of the obj Class are serializable:
    => list, dictionary, string, integer and boolean
    """

    return obj.__dict__
