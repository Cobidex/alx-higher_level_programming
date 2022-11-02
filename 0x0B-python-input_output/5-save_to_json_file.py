#!/usr/bin/python3
'''module to write to file in json'''


import json


def save_to_json_file(my_obj, filename):
    '''writes json text to file'''
    with open(filename, mode="w", encoding="utf-8") as my_file:
        obj = json.dumps(my_obj)
        my_file.write(obj)
