#!/usr/bin/python3
"""
    A square class with a parameter size type int that raises TypeError msg 
    if the type is not int and raises a ValueError when the size is less than zero(0)
"""
class Square:
    """
        A square class with a parameter size type int that raises TypeError msg 
        if the type is not int and raises a ValueError when the size is less than zero(0)
    """
    def __init__(self, size=0):
        """
        A square class with a parameter size type int that raises TypeError msg 
        if the type is not int and raises a ValueError when the size is less than zero(0)
        args:
            param1 (int): This is the First Parameter
        """
        self.__size = size
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")