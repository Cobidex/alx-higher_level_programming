#!/usr/bin/python3
'''Rectangle module
'''


from models.base import Base


class Rectangle(Base):
    '''class rectangle inherits base class
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initializing class object
        '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self, width):
        '''getter
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getter
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''setter
        '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''setter
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
