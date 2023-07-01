#!/usr/bin/python3
"""This module provides a class that defines a rectangle."""


class Rectangle:
    """
    Represents a rectangle.

    Attributes:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            The width of the rectangle (int).
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            The height of the rectangle (int).
        """
        return self.__height

    @width.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle (int).
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle (int).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        Generate a string representation of the rectangle.

        Returns:
            A string representation of the rectangle.
        """
        rect = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append("#")
                if j == self.__width - 1 and i != self.__height - 1:
                    rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        """
        A string representation of the rectangle that can be
        used to recreate the object.

        Returns:
            A string representation of the rectangle.
        """
        rect = f"Rectangle({self.__width}, {self.__height})"
        return rect

    def __del__(self):
        """
        Clean up resources associated with the rectangle object.

        This method is called when the rectangle object
        is about to be destroyed.
        It prints a farewell message indicating that the
        rectangle is being deleted.
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
