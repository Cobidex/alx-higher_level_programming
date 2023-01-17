#!/usr/bin/python3
'''module for making request'''

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        html = html.decode()
        print('Body response:')
        for line in html.split('\n'):
            print('\t- {}'. format(line))
