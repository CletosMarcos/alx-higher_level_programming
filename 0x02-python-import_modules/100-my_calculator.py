#!/usr/bin/python3

from calculator_1 import add, sub, div, mul
from sys import argv

if __name__ == "__main__":

    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    elif op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
        exit(0)

    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
        exit(0)

    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
        exit(0)

    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
        exit(0)
