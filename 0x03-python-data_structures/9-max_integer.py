#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max_nr = my_list[0]

        for nr in my_list:
            if nr > max_nr:
                max_nr = nr

        return max_nr
