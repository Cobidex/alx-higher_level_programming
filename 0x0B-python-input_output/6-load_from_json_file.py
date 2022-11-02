#!/usr/bin/python3
'''module to read json file'''


import json


def load_from_json_file(filename):
    '''create object from jason file'''
    with open(filename, "r") as my_file:
        return json.loads(my_file.read())
