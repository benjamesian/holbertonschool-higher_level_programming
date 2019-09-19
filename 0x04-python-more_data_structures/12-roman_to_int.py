#!/usr/bin/python3
def roman_to_int(roman_string):
    s = 0
    current = 0
    d = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1}
    for c in reversed(roman_string):
        if d[c] < current:
            s -= d[c]
        else:
            s += d[c]
        current = d[c]
    return s
