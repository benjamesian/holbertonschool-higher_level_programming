#!/usr/bin/python3
"""
Divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Divide all elements in a matrix by a value """
    if not isinstance(matrix, list):
        t_err()
    if not all(isinstance(x, list) for x in matrix):
        t_err()
    if not all(isinstance(x, int) or isinstance(x, float)
               for y in matrix for x in y):
        t_err()
    if matrix:
        size = len(matrix[0])
        if not all(len(x) == size for x in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in y] for y in matrix]


def t_err():
    """ TypeError with a message """
    raise TypeError("matrix must be a matrix (list of lists) of\
    integers/floats")
