#!/usr/bin/python3
"""Defines a class named Square with attribute: size,
methods: area and my_print as well as getters & setters
"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Returns the area of the Square"""
        return self.__size ** 2

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

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
