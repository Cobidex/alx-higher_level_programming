#!/usr/bin/python3
'''a module for json-string function'''


import json


def from_json_string(my_str):
    '''returns python object'''
    return json.loads(my_str)
