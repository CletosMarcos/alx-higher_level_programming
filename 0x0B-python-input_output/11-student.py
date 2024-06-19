#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

            args:
                attr: If attrs is a list of strings, only attribute names
                contained in this list must be retrieved.

                Otherwise, all attributes must be retrieved
            """

        retrieved = {}

        if type(attrs) is list and all(isinstance(pos, str) for pos in attrs):
            retrieved = {key: self.__dict__[key] for key in attrs
                         if key in self.__dict__}
            return retrieved

        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
