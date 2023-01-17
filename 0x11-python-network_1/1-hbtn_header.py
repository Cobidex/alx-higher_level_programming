#!/usr/bin/python3
'''module for the 1-hbtn_header.py'''

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
