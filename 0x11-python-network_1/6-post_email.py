#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': arg[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
