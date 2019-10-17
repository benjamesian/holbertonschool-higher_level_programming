#!/usr/bin/python3
""" mod doc """


def read_lines(filename="", nb_lines=0):
    """ func doc """
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            while nb_lines > 0:
                nb_lines -= 1
                print(f.readline(), end='')
