#!/usr/bin/python3
"""Defines a class named Square with attribute: size,
methods: area and my_print as well as getters & setters
"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor of a Square with the size and position"""
        self.size = size
        self.position = position

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
        """ Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """Getter of the private attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the private attribute position"""
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(element, int) for element in value) \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
