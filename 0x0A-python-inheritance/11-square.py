#!/usr/bin/python3
""" module that defines a class Square"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
        defines a square
    """

    def __init__(self, size):
        """
            Initializes the super() class with square size
            using <integer_validator> to validade size

            args:
                size
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
