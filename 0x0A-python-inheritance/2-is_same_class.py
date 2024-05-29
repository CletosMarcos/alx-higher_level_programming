#!/usr/bin/python3

"""Module that defines a function is_same_class"""


def is_same_class(obj, a_class):
    """ returns True if the object is exactly an instance of the
        specified class ; otherwise False """
    if isinstance(obj, a_class):
        return True

    return False
