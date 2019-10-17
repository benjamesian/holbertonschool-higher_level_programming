#!/usr/bin/python3
""" mod doc """


def read_lines(filename="", nb_lines=0):
    """ func doc """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines(nb_lines)
        for line in lines:
            print(line, end='')
