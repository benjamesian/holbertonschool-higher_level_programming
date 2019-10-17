#!/usr/bin/python3
""" mod doc """


def write_file(filename="", text=""):
    """ func doc """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
