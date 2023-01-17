#!/usr/bin/python3
'''
    script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with
    the letter as a parameter.
'''

import sys
import requests


if __name__ == "__main__":
    if len(argv) == 1:
        my_dict = {'q': ""}
    else:
        my_dict = {'q': sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', data=my_dict)
    j = req.json()
    if req.headers.get('content-type') != 'application/json':
        print('Not a valid JSON')
    elif len(j) == 0:
        print('No result')
    else:
        print('[{}] {}'.format(d['id'], d['name']))
