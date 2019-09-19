#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_list = sorted(my_list)
    for i, el in enumerate(my_list):
        if i > 0 and el == my_list[i - 1]:
            continue
        print(el)
        sum += el

    return sum
