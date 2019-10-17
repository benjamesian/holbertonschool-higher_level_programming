#!/usr/bin/python3
""" mod doc """


def save_to_json_file(my_obj, filename):
    """ func doc """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
