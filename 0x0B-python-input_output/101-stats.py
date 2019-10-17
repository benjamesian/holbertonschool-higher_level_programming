#!/usr/bin/python3
"""mod doc"""
import sys


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
            print(f'File size: {size}')
            for key in sorted(d):
                print(f'{key}: {d[key]}')

        except KeyboardInterrupt as inst:
            print(f'File size: {size}')
            for key in sorted(d):
                print(f'{key}: {d[key]}')

            raise inst
