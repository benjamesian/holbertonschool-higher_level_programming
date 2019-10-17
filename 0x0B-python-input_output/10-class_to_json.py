#!/usr/bin/python3
""" mod doc """
import json


def class_to_json(obj):
    """ func doc """
    return json.dumps(obj.__dict__)
