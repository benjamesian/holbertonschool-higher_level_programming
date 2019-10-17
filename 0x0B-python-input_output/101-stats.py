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
    while True:
        try:
            for i in range(10):
                line = sys.stdin.readline().split()
                if line:
                    d[line[-2]] = d.get(line[-2], 0) + 1
                    size += int(line[-1])
            my_print(d, size)
        except KeyboardInterrupt as inst:
            my_print(d, size)
            raise inst
