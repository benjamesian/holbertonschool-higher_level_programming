#!/usr/bin/python3
ord_a = ord('a')
for el in range(ord_a, ord_a + 26):
    if chr(el) != 'q' and chr(el) != 'e':
        print(chr(el), end='')
