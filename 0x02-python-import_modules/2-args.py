#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    if len(argv) - 1 == 1:
        print("1 argument:")
    elif len(argv) - 1 == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv) - 1))

    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
