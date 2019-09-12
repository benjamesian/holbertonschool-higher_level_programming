#!/usr/bin/python3
import sys
from functools import reduce

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        print("0")
    else:
        print("{}".format(reduce(lambda x, y: x + y, map(int, sys.argv[1:]))))
