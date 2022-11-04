#!/usr/bin/python3
'''Rectangle module
'''


import base


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
