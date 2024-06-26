#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    except TypeError:
        return False
    except NameError:
        return False
    else:
        return True
