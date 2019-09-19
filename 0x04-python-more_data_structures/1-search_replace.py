#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = my_list[:]
    for i, el in enumerate(my_list):
        if el == search:
            my_list[i] = replace

    return my_list
