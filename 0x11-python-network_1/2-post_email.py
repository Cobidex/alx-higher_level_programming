#!/usr/bin/python3
'''contain the python script module'''

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    coded = urllib.parse.urlencode(value).encode('ascii')
    req = urllib.request.Request(url, data=coded, method='POST')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html = html.decode('utf-8')
        print(html)
