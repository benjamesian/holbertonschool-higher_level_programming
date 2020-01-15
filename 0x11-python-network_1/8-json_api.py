#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    payload = {'q': '' if len(argv) <= 1 else argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        j = r.json()
        if not j:
            print('No result')
        else:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
    except ValueError as e:
        print('Not a valid JSON')
