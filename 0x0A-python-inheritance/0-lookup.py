#!/usr/bin/python3

"""module to return a list of attributes and methods"""


def lookup(obj):
    """Return a list of available attributes and methods of an object
    args:
        obj: object to be considered
        """

    return list(sorted(obj.__dict__))
