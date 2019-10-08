#!/usr/bin/python3
""" N Queens """
import sys

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    # I dont know anything about this problem :P
