#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    (a_dictionary.pop(k) for k in filter(lambda x: a_dictionary[x] == value, a_dictionary))
    return a_dictionary
