#!/usr/bin/python3

"""Prints a square"""


def print_square(size):
    """
    Prints a square of size "size"

    args:
        size: size of the square

        size must be an integer and >= 0 otherwise,
        raise a ValueError
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0: print() # as it doen't enter the loop

    for i in range(size):
        print("#" * size)
