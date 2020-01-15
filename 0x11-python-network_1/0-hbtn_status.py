#!/usr/bin/python3
from urllib import request

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()
        print('Body response:')
        print('\t- type: {:s}'.format(str(type(content))))
        print('\t- content: {:s}'.format(str(content)))
        print('\t- utf8 content: {:s}'.format(content.decode('utf-8')))
