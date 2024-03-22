#!/usr/bin/python3

f_add = __import__('add_0').add

if __name__ == "__main__":
    f_add.a = 1
    f_add.b = 2

    print("{} + {} = {}".format(f_add.a, f_add.b, f_add(f_add.a, f_add.b)))
