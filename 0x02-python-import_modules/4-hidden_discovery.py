#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    so = dir(hidden_4)
    s = sorted(filter(lambda x: x[:2] != "__", so))
    for el in s:
        print(el)
