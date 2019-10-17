#!/usr/bin/python3
""" mod doc """
import json


def load_from_json_file(filename):
    """ func doc """
    with open(filename, 'r') as f:
        return json.load(f)
    return None
