#!/usr/bin/python3
""" module that defines a class BaseGeometry"""

from "7-base_geometry" import BaseGeometry


class Rectangle(BaseGeometry):
    """
        defines a method that raises an exception

        methods:
                area(): raises an exception with the
                msg "area() is not implemented"
    """

    def __init__(self, width, height):
        """
            Initializes the width and height
            and making sure the values are valid by using the
            method <integer_validator>
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
