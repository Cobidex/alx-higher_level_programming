#!/usr/bin/python3
'''
    module contains file append function
'''


def append_write(filename="", text=""):
    '''appends to a file'''

    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
