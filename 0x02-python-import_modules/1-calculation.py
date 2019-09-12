#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    for op in ((add, "+"), (sub, "-"), (mul, "*"), (div, "/")):
        print("{} {} {} = {}".format(a, op[1], b, op[0](a, b)))
