#!/usr/bin/python3
import sys

if __name__ == "__main__":
    nargs = len(sys.argv)
    if nargs == 1:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(nargs - 1, "" if nargs == 2 else "s"))
        for i, el in enumerate(sys.argv[1:]):
            print("{}: {}".format(i + 1, el))
