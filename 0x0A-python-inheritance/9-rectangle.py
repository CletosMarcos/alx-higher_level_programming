#!/usr/bin/python3
""" module that defines a class Rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
        defines a Rectanglee
        
        args:
            width
            height

        methods:
                area()
                __str__
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

    def area(self):
        """
            implementation of the function
            returns: the rectangle area
        """

        return self.__width * self.__height

    def __str__(self):
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
