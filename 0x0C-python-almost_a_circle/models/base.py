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
        """ returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__+".json", 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string(None))
            else:
                list_dicts = []
                [list_dicts.append(obj.to_dictionary()) for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary:
            if cls.__name__ = "Rectangle":
                dummy_instance = cls(1, 1)
            else:
                dummy_instance = cls(1)
            return dummy_instance.update(**dictionary)
