#!/usr/bin/python3
""" mod doc """


def number_of_lines(filename=""):
    """ func doc """
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())
