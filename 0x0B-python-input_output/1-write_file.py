#!/usr/bin/python3
"""defines a function write_file()"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and
        returns the number of characters written

        args:
            filename: file to operate
            text: the string to write to the file
    """

    with open(filename, mode="w", encoding="utf-8") as wfile:
        return wfile.write(text)
