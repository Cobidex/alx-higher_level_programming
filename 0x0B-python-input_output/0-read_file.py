#!/usr/bin/python3
'''
    module contains file read function
'''


def read_file(filename=""):
    '''Reads a file'''

    with open(filename, 'r', encoding="utf-8") as my_file:
        my_string = my_file.read()
        print(my_string, end="")
