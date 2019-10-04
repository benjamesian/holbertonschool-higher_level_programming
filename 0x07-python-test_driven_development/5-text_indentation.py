#!/usr/bin/python3
"""
Text with indentation
"""


def text_indentation(text):
    """ Format and print a string """
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
    text = text.strip()
    if text and any(text[-1] == x for x in ['.', '?', ':']):
        text += '\n\n'
    print(text, end='')
