#!/usr/bin/python3
'''module to read json file'''


import json


def load_from_json_file(filename):
    '''create object from jason file'''
    with open(filename, mode="r", encoding "utf-8") as my_file:
        obj = my_file.read()
        json.loads(obj)
        return obj