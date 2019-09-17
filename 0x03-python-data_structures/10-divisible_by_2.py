#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return list(map(lambda x: not bool(x % 2)))
