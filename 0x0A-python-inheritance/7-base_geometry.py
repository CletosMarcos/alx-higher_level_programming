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

    def integer_validator(self, name, value):
        """
            validates value

            args:
                name: always a string
                value:
                    if not an integer: raise a TypeError exception
                    if less or equal to 0: raise a ValueError exception
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
