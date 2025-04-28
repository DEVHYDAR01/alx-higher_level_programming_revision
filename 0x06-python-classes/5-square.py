#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size
    
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
    
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print("", end="\n")



my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")


# for i in range(3):
#     for j in range(3):
#         print("#", end="")
#     print()