#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    return (l, None if l == 0 else sentence[0])
