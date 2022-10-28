#!/usr/bin/python3
"""A module to contain class of rectangle type"""


class Rectangle():
    """class of type rectangle"""

    def __init__(self, width, height):
        """initializing class object"""

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
            self.__width = width

    @property
    def width(self):
        """retrieves value of width"""
        return self.__width

    @property
    def height(self):
        """retrieves value of height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
