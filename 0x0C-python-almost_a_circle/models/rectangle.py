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
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
