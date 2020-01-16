#!/usr/bin/python3
import requests
from sys import argv


def print_page(json):
    for result in json.get('results'):
        print(result.get('name'))
        for el in result.get('films'):
            r = requests.get(el)
            print('\t{}'.format(r.json().get('title')))

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
