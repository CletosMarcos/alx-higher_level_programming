#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    b = {}

    for i, j in a_dictionary.items():
        b[i] = j*2

    return b
