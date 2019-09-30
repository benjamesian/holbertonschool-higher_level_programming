#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_printed = 0
    n = 0

    while n < x:
        try:
            print("{:d}".format(my_list[n]), end='')
        except (TypeError, ValueError):
            n_printed -= 1
        finally:
            n_printed += 1
            n += 1

    print('')

    return n_printed
