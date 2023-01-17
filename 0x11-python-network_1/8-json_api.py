#!/usr/bin/python3
'''
    script that takes in a letter and sends a POST
    request to http://0.0.0.0:5000/search_user with
    the letter as a parameter.
'''

import sys
import requests


if __name__ == "__main__":
    my_dict = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    req = requests.post("http://0.0.0.0:5000/search_user", data=my_dict)
    try:
        j_dict = req.json()
        if j_dict:
            print("[{}] {}". format(j_dict.get("id"), j_dict.get("name")))
        else:
            print("No result")
    except TypeError:
        print("Not a valid JSON")
