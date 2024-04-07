#!/usr/bin/python3

def uniq_add(my_list=[]):
    set_uniq = set(my_list)
    sum = 0

    for i in set_uniq:
        sum += i

    return sum
