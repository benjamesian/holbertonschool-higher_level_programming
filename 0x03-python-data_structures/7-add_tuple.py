#!/usr/bin/python3
from itertools import zip_longest
def add_tuple(tuple_a=(), tuple_b=()):
    l = list(zip_longest(tuple_a, tuple_b, (0,0), fillvalue=0))
    return (sum(l[0]), sum(l[1]))
