#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    nargs = len(sys.argv)
    if nargs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a1 = sys.argv[1]
    op = sys.argv[2]
    a2 = sys.argv[3]

    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    ops = [
        ("+", add),
        ("-", sub),
        ("*", mul),
        ("/", div)
    ]
    for oper in ops:
        if op == oper[0]:
            result = oper[1](int(a1), int(a2))
    print("{} {} {} = {}".format(a1, op, a2, result))
