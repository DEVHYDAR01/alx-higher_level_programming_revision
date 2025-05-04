#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.size = size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        current_square_area = self.__size **2
        return current_square_area