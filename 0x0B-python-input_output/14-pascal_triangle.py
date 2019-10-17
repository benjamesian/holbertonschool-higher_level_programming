#!/usr/bin/python3
""" mod doc """


def pascal_triangle(n):
    """ func doc """
    l = []
    if n <= 0:
        return l
    for i in range(1, n + 1):
        inner = []
        for j in range(i):
            if 0 < j < i - 1:
                inner.append(l[-1][j - 1] + l[-1][j])
            else:
                inner.append(1)
        l.append(inner)
    return l
