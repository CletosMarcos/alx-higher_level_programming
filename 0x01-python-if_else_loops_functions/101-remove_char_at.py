#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ""

    if len(str) == 0:
        return str
    elif n < 0 or n > len(str):
        return str
    else:
        for i in range(len(str)):
            if i != n:
                new_str += str[i]

        return new_str
