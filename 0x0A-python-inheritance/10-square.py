#!/usr/bin/python3
"""
This module defines the Square class that inherits from the
Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class represents a square and inherits from the Rectangle class.
    """
    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square (both width and height).
        """
        super().integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
