#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        s = ("{:d} " * len(row)).strip()
        print(s.format(*row))
