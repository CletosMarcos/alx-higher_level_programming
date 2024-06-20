#!/usr/bin/python3
"""Defines a function append_after()"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file,
        after each line containing a specific string

        Args:
            filename (string): name of the file
            search_string: the specific string to be searched
            new_string: the string to insert in case the above string is found
    """

    with open(filename, mode='a', encoding='utf-8') as fn:
        for line in fn:
            if search_string in line:
                fn.write(new_string)
