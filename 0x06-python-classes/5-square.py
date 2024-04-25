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

    """ Prints the square with the character #."""
    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
