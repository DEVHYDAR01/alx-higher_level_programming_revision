#!/usr/bin/python3
"""
square.py: This module defines a Square class that supports size validation,
area calculation, and comparison operations based on the area.
"""

class Square:
    """
    Represents a square with a numerical size.

    Attributes:
        __size (int or float): The length of the square's side.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int or float, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number (int or float).
            ValueError: If size is negative.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int or float: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int or float): The new size of the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is negative.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int or float: The area of the square.
        """
        return self.size ** 2

    def __lt__(self, other):
        """
        Checks if this square is less than another based on area.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if this square's area is less, else False.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if this square is less than or equal to another based on area.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if this square's area is less than or equal, else False.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Checks if this square is equal to another based on area.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if both squares have the same area, else False.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if this square is not equal to another based on area.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if squares have different areas, else False.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if this square is greater than another based on area.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if this square's area is greater, else False.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if this square is greater than or equal to another based on area.

        Args:
            other (Square): The square to compare to.

        Returns:
            bool: True if this square's area is greater than or equal, else False.
        """
        return self.area() >= other.area()
