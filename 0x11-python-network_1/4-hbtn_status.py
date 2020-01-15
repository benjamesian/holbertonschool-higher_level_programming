#!/usr/bin/python3
import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {:s}'.format(r.encoding))
    print('\t- content: {:s}'.format(r.content.decode('utf-8')))
