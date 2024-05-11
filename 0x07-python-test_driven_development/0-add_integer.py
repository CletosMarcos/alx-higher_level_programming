#!/usr/bin/python3

"""
module containing an ADD function
"""


def add_integer(a, b=98):
    """ computes the addition of a and b

        Args: a and b must be integer or float
              if not must raise TypeError Exception
        Return: an integer a + b
    """

    typevar = [int, float]

    if type(a) not in typevar:
        raise TypeError("a must be an integer")
    if type(b) not in typevar:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
