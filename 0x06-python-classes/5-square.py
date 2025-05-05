#!/usr/bin/python3
"""
square.py: This module defines a Square class that models a square, allows size validation,
computes its area, and prints a visual representation using `#` characters.
"""

class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The length of the square's side (must be a non-negative integer).
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets a new value for the square's size with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        current_square_area = self.__size ** 2
        return current_square_area

    def my_print(self):
        """
        Prints the square using the `#` character.

        Prints an empty line if the size is 0. Otherwise, prints rows of `#` where
        the number of rows and columns equals the size.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)