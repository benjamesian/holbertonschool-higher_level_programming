#!/usr/bin/python3
def uppercase(str):
    lowers = range(ord('a'), ord('z') + 1)
    for i, c in enumerate(str):
        up_c = chr(ord(c) - ord('a') + ord('A'))
        print("{}".format(up_c if ord(c) in lowers else c), end='')
    print("")
