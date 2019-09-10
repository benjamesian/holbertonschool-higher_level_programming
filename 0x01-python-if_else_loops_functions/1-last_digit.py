#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = (abs(number) % 10) * (-1 if number < 0 else 1)
if ld == 0:
    tail = "zero"
elif ld > 5:
    tail = "greater than 5"
else:
    tail = "less than 6 and not zero"
print("Last digit of {} is {} and is {}".format(number, ld, tail))
