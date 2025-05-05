#!/usr/bin/python3
"""
square.py: This module defines a Square class that models a square with a given
size and position offset. It can compute its area and print a visual representation.
"""

class Square:
    """
    Represents a square with size and position.

    Attributes:
        __size (int): The size of the square (must be a non-negative integer).
        __position (tuple): A tuple of two positive integers representing the
                            horizontal and vertical offset when printing.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position offset as a tuple of two
                                        non-negative integers. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not a valid tuple.
            ValueError: If size is negative.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The (x, y) position offset for printing.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): A tuple of two non-negative integers.

        Raises:
            TypeError: If value is not a tuple of two non-negative integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the `#` character, taking into account its position.

        If size is 0, it prints an empty line.
        """
        print(self.__str__())

    def __str__(self):
        """
        Returns a string representation of the square, considering position offset.

        Returns:
            str: A formatted string displaying the square with the correct alignment.
        """
        if self.__size == 0:
            return ""

        lines = [""] * self.__position[1]  # Vertical offset
        for _ in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            lines.append(line)
        return "\n".join(lines)
