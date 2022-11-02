#!/usr/bin/python3
'''
    module contains file write function
'''


def write_file(filename="", text=""):
    '''writes to a file'''

    with open(filename, 'w', encoding="utf-8") as my_file:
        return my_file.write(text)
