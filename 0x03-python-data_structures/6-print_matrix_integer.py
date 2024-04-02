#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        row_size = len(row)
        count = 0

        for col in row:
            count += 1

            if count < row_size:
                print("{}".format(col), end=" ")
            else:
                print("{}".format(col), end="")

        print()
