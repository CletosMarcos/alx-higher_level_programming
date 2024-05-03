#!/usr/bin/python3

""" Defines a class Square."""


class Square:
    """ Initializes the square."""
    def __init__(self, size=0):
        self.__size = size

    """ size getter method."""
    @property
    def size(self):
        return self.__size

    """ size setter."""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ Determines the current area."""
    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        """Verify based on Square area if instances are equal."""
        return self.__size == other.__size

    def __ne__(self, other):
        """Verify if instances area is (!=) Not equal/different."""
        return self.__size != other.__size

    def __gt__(self, other):
        """Verify if instances area are >."""
        return self.__size > other.__size

    def __lt__(self, other):
        """Verify is instances area are >."""
        return self.__size < other.__size

    def __le__(self, other):
        """Verify if instances are are <=."""
        return self.__size <= other.__size

    def __ge__(self, other):
        """verify if instancesarea are >=."""
        return self.__size >= other.size
