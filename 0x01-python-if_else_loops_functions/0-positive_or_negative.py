#!/usr/bin/python3
import random
number = random.randint(-10, 10)
word = "negative" if number < 0 else "zero" if number == 0 else "positive"
print("{} is {}".format(number, word))
