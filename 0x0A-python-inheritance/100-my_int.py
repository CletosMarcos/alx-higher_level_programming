#!/usr/bin/python3

"""module that defines a Class MyInt that inherits from int"""


class MyInt(int):
    """
        MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True
