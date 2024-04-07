#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    ret_matrix = []
    for i in matrix:
        new_matrix = []
        for j in i:
            new_matrix.append(j**2)
        ret_matrix.append(new_matrix)

    return ret_matrix
