#!/usr/bin/python3
import requests
from sys import argv

if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    r = requests.get(url)
    json = r.json()
    for el in json[:10]:
        print("{}: {}".format(
            el.get('sha'),
            el.get('commit').get('author').get('name')))
