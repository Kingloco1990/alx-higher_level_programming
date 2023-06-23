#!/usr/bin/python3
"""A class named Square with attribute: size, method: area as well as
getters & setters. The class creation was done making use of special methods
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
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method to get the area of the Square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Returns the results for comparing two areas with (==)"""
        return self.area() == other.area()

    def __ne__(self, other):
        """ Returns the results for comparing two areas with (!=)"""
        return self.area() != other.area()

    def __gt__(self, other):
        """ Returns the results of comparing two areas with (>)"""
        return self.area() > other.area()

    def __ge__(self, other):
        """ Returns the results of comparing two areas with (>=)"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """ Returns the results of comparing two areas with (<)"""
        return self.area() < other.area()

    def __le__(self, other):
        """ Returns the results of comparing two areas with (<=)"""
        return self.area() <= other.area()

