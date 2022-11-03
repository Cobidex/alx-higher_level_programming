#!/usr/bin/python3
'''module for a class of student'''


class Student():
    '''creates a class of type student'''

    def __init__(self, first_name, last_name, age):
        '''initializes the class object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary rep of class object'''
        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            temp = {}
            for item in attrs:
                if not isinstance(item, str):
                    return self.__dict__
                if item in self.__dict__.keys():
                    temp[item] = self.__dict__[item]
            return temp
