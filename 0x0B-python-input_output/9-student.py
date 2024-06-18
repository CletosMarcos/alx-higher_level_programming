#!/usr/bin/python3

"""Defines a class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        first_name = first_name
        last_name = last_name
        age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""

        return type(self).__dict__
