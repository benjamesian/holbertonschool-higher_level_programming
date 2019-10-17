#!/usr/bin/python3
""" mod doc """


def append_after(filename="", search_string="", new_string=""):
    """ func doc """
    text = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
