#!/usr/bin/python3
"""defines a function append_write"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8) and
        returns the number of characters added

        args:
            filename: the name of the file
            text: the string to append to the file
    """

    with open(filename, mode="a", encoding="utf-8") as afile:
        return afile.write(text)
