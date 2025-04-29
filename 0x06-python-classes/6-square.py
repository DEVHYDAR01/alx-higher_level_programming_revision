#!/usr/bin/python3
class Square:
    """
    A class to represent a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): A tuple representing the horizontal and vertical positions (x, y) where the square should be printed.

    Methods:
        area(): Returns the area of the square.
        my_print(): Prints the square at the specified position with the given size.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The (x, y) position of the square. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: A tuple (x, y) representing the position of the square.
        """
        return self.__position
    
    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): A tuple (x, y) representing the new position.

        Raises:
            TypeError: If the position is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value 
        
    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Prints the square at the specified position with the given size.

        Prints an empty line based on the vertical position (position[1]).
        Then prints the square with spaces before each row based on the horizontal position (position[0]).

        If the size of the square is 0, nothing is printed.
        """
        # First, print the vertical space (empty lines) based on position[1]
        for _ in range(self.__position[1]):
            print()  # Blank line for vertical position

        # Now, print the square with the correct horizontal positioning
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)