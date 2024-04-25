#!/usr/bin/python3

""" Defines a class Square."""


class Square:
    """ Initializes the square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """ position getter method."""
    @property
    def position(self):
        return self.__position

    """ position setter method."""
    @position.setter
    def position(self, value):
        if (type(value) is tuple and
                len(value) == 2 and
                type(value[0]) is int and
                type(value[1]) is int and
                value[0] >= 0 and
                value[1] >= 0):

            self.__position = value

        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """ Determines the current area."""
    def area(self):
        return self.__size ** 2

    """ Prints the square with the character #."""
    def my_print(self):
        if self.__size == 0:
            print()
            return

        [print() for p in range(self.__position[1])]

        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print()
