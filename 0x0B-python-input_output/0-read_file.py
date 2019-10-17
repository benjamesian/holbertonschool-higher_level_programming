#!/usr/bin/python3
""" mod doc """


def read_file(filename=""):
    """ func doc """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
