#!/usr/bin/python3

"""A module that computes and returns the division of all
elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides matrix with div

    args:
        matrix - list of lists, with all rows being the same size
               - the lists contains only ints or floats

        div - value used to divide the matrix
            - can be int or float

    return: a new matrix containing the results of the division,
            rounded by 2 decimal places
    """

    types = [int, float]
    msg = "matrix_divided() missing 1 required positional argument: 'matrix'"
    msg_2 = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(msg)

    if type(matrix) is not list:
        raise TypeError(msg_2)

    for i in matrix:
        if type(i) is not list:
            raise TypeError(msg_2)
        elif len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for j in i:
                if type(j) not in types:
                    raise TypeError(msg_2)

    if type(div) not in types:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrx = []

    for i in matrix:
        temp_mtrx = []

        [temp_mtrx.append(round(j/div, 2)) for j in i]

        new_matrx.append(temp_mtrx)

    return new_matrx
