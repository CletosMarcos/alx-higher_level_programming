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

    pos = 0
    new_text = ""
    chars = (".", ":", "?")

    while pos < len(text) and text[pos] == " ":
        pos += 1

    while pos < len(text):
        if text[pos] == " " and text[pos - 1] == " ":
            pos += 1
            continue
        if text[pos] == " " and text[pos - 1] == "\n":
            pos += 1
            continue
        if text[pos] == " " and text[pos + 1] == "\n":
            pos += 1
            continue
        new_text += text[pos]
        if text[pos] in chars:
            new_text += "\n\n"
            pos += 1

        pos += 1

    print(new_text, end="")
