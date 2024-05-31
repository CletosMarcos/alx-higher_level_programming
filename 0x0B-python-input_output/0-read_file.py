#!/usr/bin/python3
"""Defines a function read_file()"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
        args:
            filename: file to be read
    """

    with open(filename, encoding='utf-8') as nfile:
        for line in nfile:
            print(line)
