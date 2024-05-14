#!/usr/bin/python3

"""
ext Indentation
This module provides a funcion that prints a text with 2 new lines after each
of these characters `. ? :`
"""


def text_indentation(text):
    """ Prints two new Lines if it finds the following chars ". : ?"

    args:
        text: test provided
        => text must be a string

    Raises:
        TypeError if the argument text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    new_text = ""
    chars = (".", ":", "?")

    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
