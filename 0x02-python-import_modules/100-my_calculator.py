#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    def do_calc(a, op, b):
        ops = [
            ("+", add),
            ("-", sub),
            ("*", mul),
            ("/", div)
        ]

        for oper in ops:
            if op == oper[0]:
                return oper[1](int(a), int(b))
        return None

    nargs = len(sys.argv)
    if nargs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(*sys.argv[1:], do_calc(*sys.argv[1:])))
