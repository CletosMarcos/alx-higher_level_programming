#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    res_tuple = ()

    if len(tuple_a) >= 2:
        if len(tuple_b) >= 2:
            res_tuple = (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])
        elif not tuple_b:
            res_tuple = (tuple_a[0], tuple_a[1])
        else:
            res_tuple = (tuple_a[0]+tuple_b[0], tuple_a[1])

    elif len(tuple_b) >= 2:
        if not tuple_a:
            res_tuple = (tuple_b[0], tuple_b[1])
        else:
            res_tuple = (tuple_a[0]+tuple_b[0], tuple_b[1])

    elif not tuple_a and not tuple_b:
        res_tuple = (0, 0)

    elif not tuple_a:
        res_tuple = (tuple_b[0], 0)

    elif not tuple_b:
        res_tuple = (tuple_a[0], 0)

    else:
        res_tuple = (tuple_a[0]+tuple_b[0], 0)

    return res_tuple
