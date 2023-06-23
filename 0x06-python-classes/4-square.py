#!/usr/bin/python3
"""A class named Square with attribute: size, method: area as well as
getters & setters
"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter of the private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the private attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method to get the area of the Square"""
        return self.__size ** 2
