#!/usr/bin/python3

"""A module that defines a  class that inherits from list
    methods:
            print_sorted(): returns the sorted list
            """


class MyList(list):
    """inherits from list"""

    def print_sorted(self):
        """prints the sorted list"""

        return print(sorted(self))
