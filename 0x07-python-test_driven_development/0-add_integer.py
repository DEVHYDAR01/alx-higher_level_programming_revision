#!/usr/bin/bash
""" 
This module will compute a function that adds 2 integers. 
"""
def add_integer(a, b=98):
    """
    args:
        param1 a(int, float): This is the first parameter
        param2 b(int, float): This is the second parameter
    returns:
        if a is an instance of float then a is type casted to int same for b too.
        The sum of a and b
    raises:
        A typeError if a is not an instance of int or float
        A typeError if b is not an instance of int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)