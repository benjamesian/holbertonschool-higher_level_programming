#!/usr/bin/python3
from urllib import request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    with request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
