#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from the
BaseGeometry class.
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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns string representation of an instance of class square"""
        return f"[{type(self).__name__}] {self.__size}/{self.__size}"
