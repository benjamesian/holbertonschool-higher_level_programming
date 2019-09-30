#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n_printed = 0
    while n_printed < x:
        try:
            print(my_list[n_printed], end="")
            n_printed += 1
        except IndexError:
            break

    print('')

    return n_printed
