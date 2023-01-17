#!/usr/bin/python3
'''
    script that takes your GitHub
    credentials (username and password) and
    uses the GitHub API to display your id
'''

import sys
import requests


if __name__ == "__main__":
    aut = (sys.argv[1], sys.argv[2])
    u = 'https://api.github.com/user'
    req = requests.get(u, auth=aut)
    my_dict = req.json()
    print(my_dict.get('id'))
