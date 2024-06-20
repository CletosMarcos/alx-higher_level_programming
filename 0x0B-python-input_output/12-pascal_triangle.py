#!/usr/bin/python3
"""Defines a function pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
        the Pascal’s triangle of n:

        Returns an empty list if n <= 0
        You can assume n will be always an integer

        Args:
            n (int): size of the triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]  # traingle 1st row initialization

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            # Each element will be the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Then end each row with 1
        triangle.append(row)

    return triangle
