#!/usr/bin/python3
'''module for a class of student'''


class Student():
    '''creates a class of type student'''
    
    def __init__(self, first_name, last_name, age):
        '''initializes the class object'''
        self.first_name = first_name
        self.lastname = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary rep of class object'''
        return self.__dict__
