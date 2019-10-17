#!/usr/bin/python3
""" mod doc """
import json
import sys
import os.path

if __name__ == '__main__':
    fs = __import__('7-save_to_json_file').save_to_json_file
    fl = __import__('8-load_from_json_file').load_from_json_file

    filename = 'add_item.json'
    l = []
    if os.path.exists(filename):
        l = fl(filename) or []
    fs(l + sys.argv[1:], filename)
