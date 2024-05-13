#!/usr/bin/python3

"""A module to print the full name"""

def say_my_name(first_name, last_name=""):
    """
    Prints the full name if name is a string,
    otherwise raise TypeError

    args:
    first_name: person's first name
    last_name: person's last name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    """
    else:
        for i in first_name:
            if type(i) is not str:
                raise TypeError("first_name must only contain strings")
    """

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    """
    else:
        for i in last_name:
            if type(i) is not str:
                raise TypeError("last_name must only contain strings")
    """

    print(f"{first_name} {last_name}")
