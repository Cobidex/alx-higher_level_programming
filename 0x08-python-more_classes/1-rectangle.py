#!/usr/bin/python3
"""A module to contain class of rectangle type"""


class Rectangle():
    """class of type rectangle"""

    def __init__(self, width=0, height=0):
        """constructor initializing class object

        Arguments:
            width{int} -- width of rectangle (default: 0)
            height{int} -- height of rectangle (default: 0)
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("width must be an integer")
        else:
            self.__height = height
            self.__width = width

    @property
    def width(self):
        """Getter function of width

        Returns:
            int -- width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """Getter function of height

        Returns:
            height of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """setter function of width

        Arguments:
            value{int} -- value of width

        Raises:
            TypeError: width must be of type int
            ValueError: width must be >=0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter function of width

            Arguments:
                value{int} -- value of width

            Raises:
                TypeError: width must be of type int
                ValueError: width must be >=0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
