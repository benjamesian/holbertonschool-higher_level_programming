#!/usr/bin/python3
"""
Text with indentation
"""


def text_indentation(text):
    """ Pritn """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.split('.')
    text = '.\n'.join(text)
    text = text.split('?')
    text = '?\n'.join(text)
    text = text.split(':')
    text = ':\n'.join(text)
    text = text.split('\n')
    text = list(map(lambda x: x.strip(' '), text))
    text = '\n\n'.join(text)
    print(text.strip(), end='')
