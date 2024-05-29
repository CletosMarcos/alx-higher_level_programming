#!/usr/bin/python3
""" module that defines a class BaseGeometry"""


class BaseGeometry:
    """
        defines a method that raises an exception

        methods:
                area(): raises an exception with the
                msg "area() is not implemented"
    """

    def area(self):
        """
            raises an exception
        """

        raise Exception("area() is not implemented")
