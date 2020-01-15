#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    if not r.ok:
        print('Error code: {:d}'.format(r.status_code))
    else
        print(r.text)
