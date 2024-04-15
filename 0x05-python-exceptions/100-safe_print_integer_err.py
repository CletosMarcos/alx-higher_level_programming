#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))

    except TypeError as te:
        stderr.write("Exception: " + str(te) + "\n")
        return False
    except ValueError as ve:
        stderr.write("Exception: " + str(ve) + "\n")
        return False

    else:
        return True
