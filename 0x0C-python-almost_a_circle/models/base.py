#!/usr/bin/python3
"""Defines a base class of all other classes in this project"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """if: id is not None:
            * assign the public instance attribute id with this argument value
           therwise:
            * increment __nb_objects and assign the new value to the
                public instance attribute id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
