#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    output = my_list[:]
    if idx in range(len(my_list)):
        output[idx] = element
    return output
