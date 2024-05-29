#!/usr/bin/python3
""" module that defines a class Square"""

Rectangle = __import__("9-rectangle.py").Rectangle


class Square(Rectangle):
    """
        defines a square

        methods:
                area(): returns the square area
                __str__: return the square representation
    """

    def __init__(self, size:
        """
            Initializes the square size
            using <integer_validator> to validade size
        """

        self.integer_validator("size", size)
        self._sizeh = size

    def area(self):
        """
            implementation of the function
            returns: the square area
        """

        return self.__size ** 2

    def __str__(self):
        return f"[Rectangle] {self._size}/{self.__size}"
