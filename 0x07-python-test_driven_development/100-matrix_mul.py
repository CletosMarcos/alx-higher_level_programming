#!/usr/bin/python3

"""Module to multiply two matrices"""

def matrix_mul(m_a, m_b):
    """ multiplies two provided matrices

    args:
            m_a: matrix one
            m_b: matrix two

        parameters must be list of lists of ints or floats
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if  type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")

    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        if len(i) == 0:
            raise ValueError("m_a can't be empty")

    for i in m_b:
        if len(i) == 0:
            raise ValueError("m_b can't be empty")

    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")

    for i in m_b:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")

    for i in m_a:
        if len(m_a[0]) != len(i):
            raise TypeError("each row of m_a must be of the same size")

    for i in m_b:
        if len(m_b[0]) != len(i):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


    #  Solve matrix mult

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix    
