#!/usr/bin/python3
"""Defines a base class of all other classes in this project"""
import json


class Base:
    """The goal of this class is to manage `id` attribute in all your future
    classes and to avoid dulicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """if: id is not None:
            * assign the public instance attribute id with this argument value
           therwise:
            * increment __nb_objects and assign the new value to the
                public instance attribute id
        """

        if id is not None:
            self.__id = id
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("id must be an integer")
        self.__id = value

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)
