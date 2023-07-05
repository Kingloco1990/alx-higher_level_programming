#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from the
BaseGeometry class.
"""
BaseGeometry = __import__('8-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle and inherits from the
    BaseGeometry class.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: The string representation of the rectangle in the format
            '[Rectangle] width/height'.
        """
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
