#!/usr/bin/python3
"""A module for matrix dividing function"""


def matrix_divided(matrix, div):
    """returns a new matrix that is a division of the old
    Arguments:
        matrix - the matrix to divide
        div - the factor to divide by
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(err1)
    if not isinstance(matrix, list):
        raise TypeError(err1)
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(err1)
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(err1)
    lnt = len(matrix[0])
    if lnt == 0:
        raise TypeError(err1)
    for row in matrix:
        if len(row) != lnt:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
