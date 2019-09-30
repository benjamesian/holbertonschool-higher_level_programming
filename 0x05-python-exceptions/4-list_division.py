#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    n = 0

    while n < list_length:
        try:
            el = my_list_1[n] / my_list_2[n]
        except IndexError:
            el = 0
            pass
        except ZeroDivisionError:
            el = 0
            pass
        finally:
            new_list.append(el)
            n += 1

    return new_list
