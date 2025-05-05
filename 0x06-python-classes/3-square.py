#!/usr/bin/python3
"""square.py: This module defines a Square class for representing squares and computing their area."""

class Square:
    """
    Represents a square with a given side length.

    Attributes:
        __size (int): The length of a side of the square (must be a non-negative integer).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The length of a side of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.__size = size
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        current_square_area = self.__size ** 2
        return current_square_area
