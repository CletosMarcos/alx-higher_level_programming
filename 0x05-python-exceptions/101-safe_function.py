#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except IndexError:
        result = None
        stderr.write("Exception: list index out of range\n")
    except ZeroDivisionError:
        result = None
        stderr.write("Exception: division by zero\n")
    finally:
        return result
