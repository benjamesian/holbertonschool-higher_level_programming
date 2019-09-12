#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = sys.argv[2]

    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a1 = int(sys.argv[1])
    a2 = int(sys.argv[3])

    if op == "+":
        result = add(a1, a2)
    elif op == '-':
        result = sub(a1, a2)
    elif op == '*':
        result = mul(a1, a2)
    else:
        result = div(a1, a2)

    print("{:d} {} {:d} = {:d}".format(a1, op, a2, result))
