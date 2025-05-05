#!/usr/bin/python
"""
magic_class.py: This module defines a MagicClass that calculates the area of a circle
based on a given radius.
"""

class MagicClass:
    """
    Represents a circle-like structure with methods to calculate its area.

    Attributes:
        __radius (int or float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a new MagicClass instance.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number (int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates the area of the circle using πr².

        Returns:
            float: The area of the circle.
        """
        pi = 3.14
        return pi * (self.__radius ** 2)


# Test example
if __name__ == "__main__":
    magic_maths = MagicClass(4)
    print(magic_maths.area())
