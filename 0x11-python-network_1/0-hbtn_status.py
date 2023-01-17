#!/usr/bin/python3
'''module for making request'''

import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('    - type: {}'. format(type(html)))
        print('    - content: {}'. format(html))
        print('    - utf8 content: {}'. format(html.decode('utf-8')))
