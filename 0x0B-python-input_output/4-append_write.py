#!/usr/bin/python3
""" mod doc """


def append_write(filename="", text=""):
    """ func doc """
    with open(filename, 'a', encoding='utf-8') as f:
        start = f.tell()
        f.write(text)
        return f.tell() - start
    return 0
