#!/usr/bin/python3
""" mod doc """
import json
import sys


if __name__ == '__main__':
    fs = __import__('7-save_to_json_file').save_to_json_file
    fl = __import__('8-load_from_json_file').load_from_json_file

    filename = 'add_item.json'
    with open(filename, 'w') as f:
        if not f.read():
            json.dump([], f)
    obj = fl(filename)
    fs(obj.extend(sys.argv), filename)
