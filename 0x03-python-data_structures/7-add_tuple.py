#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l = list(zip(tuple_a + (0, 0), tuple_b + (0, 0)))
    return (sum(l[0]), sum(l[1]))
