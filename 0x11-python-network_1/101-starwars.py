#!/usr/bin/python3
import requests
from sys import argv

def print_page(page):
    for el in page.get('results'):
        print(el.get('name'))

if __name__ == '__main__':
    url = 'https://swapi.co/api/people/'
    payload = {'search': '' if len(argv) < 2 else argv[1]}
    r = requests.get(url, params=payload)
    json = r.json()
    print('Number of results: {}'.format(json.get('count')))

    print_page(json)
    while json.get('next'):
        r = requests.get(json.get('next'))
        json = r.json()
        print_page(json)
