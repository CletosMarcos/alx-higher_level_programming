#!/usr/bin/python3
"""Defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle that inherits from Base

        Args:
            width
            height
            x
            y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Assign each argument width, height, x and y to the right attribute
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle instance"""
        return self.height * self.width

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        x = " " * self.x  # number of columns to skip
        y = "\n" * self.y  # number of lines to skip

        print(y, end='')

        for i in range(self.height):
            print(f"{x}{'#' * self.width}")

    def __str__(self):
        """override to return [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """assigns an argument to each attribute

            * 1st argument should be the id attribute
            * 2nd argument should be the width attribute
            * 3rd argument should be the height attribute
            * 4th argument should be the x attribute
            * 5th argument should be the y attribute"""

        attr_list = ["id", "width", "height", "x", "y"]
        for arg in range(len(args)):
            setattr(self, attr_list[arg], args[arg])
