#!/usr/bin/python3
def no_c(my_string):
    return ''.join(filter(lambda x: x != 'c' and x != 'C', my_string))
