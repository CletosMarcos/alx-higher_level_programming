#!/usr/bin/python3
""" module that defines a class Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
        defines a Rectangle
        
        args:
            width
            height
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
