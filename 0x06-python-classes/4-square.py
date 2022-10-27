#!/usr/bin/python3
"""This module will create a class"""


class Square():
    """"a class of type square"""
    def __init__(self, size=0):
        """initializing quare object"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the area of a square object"""
        return self.__size * self.__size

    @property
    def size(self):
        """gets the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the square"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
