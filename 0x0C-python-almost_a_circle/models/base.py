#!/usr/bin/python3
'''
    a module to hold base class definition
'''


class Base():
    '''
        class of Base
    '''

    __nb_objects = 0
    '''private attribute'''

    def __init__(self, id=None):
        '''
            initializing class object
        '''

        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
