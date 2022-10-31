#!/usr/bin/python3
"""
add_function - adds two integers
parameter a: int
parameter b: int set to 98 default
"""


def add_integer(a, b=98):
    """
    adds two integers
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
