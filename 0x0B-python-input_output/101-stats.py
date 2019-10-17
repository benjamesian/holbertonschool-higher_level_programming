#!/usr/bin/python3
"""mod doc"""
import sys


def my_print(d, size):
    """ formatted printing """
    print('File size: {:d}'.format(size))
    for key in sorted(d):
        print('{:s}: {:d}'.format(key, d[key]))

if __name__ == '__main__':
    d = {}
    size = 0
    leave = False
    while True:
        try:
            for i in range(10):
                line = sys.stdin.readline()
                if line:
                    arr = line.split()
                    d[arr[-2]] = d.get(arr[-2], 0) + 1
                    size += int(arr[-1])
                else:
                    leave = True
                    break
            my_print(d, size)
            if leave:
                break
        except KeyboardInterrupt as inst:
            my_print(d, size)
            raise inst
