#!/usr/bin/python3
"""
This module provides the Square class, which represents a square shape.
It inherits properties and methods from the Rectangle class
and extends it to handle square-specific attributes and behaviors.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a Square, which inherits from the Rectangle class.

    Args:
        Rectangle (type): The parent class to inherit from.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square's side.
            x (int, optional): The x-coordinate of the square's position.
            Default is 0.
            y (int, optional): The y-coordinate of the square's position.
            Default is 0.
            id (int, optional): An identifier for the square. Default is None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Retrieves the size of the square's side.

        Returns:
            int: The size of the square's side.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square's side.

        Args:
            value (int): The new size of the square's side.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A formatted string containing the square's id, position,
            and size.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Update the square's attributes.

        Args:
            *args: Variable length argument list. The first argument can be an
            integer id, and subsequent arguments can be size, x, and y values.

            **kwargs: Arbitrary keyword arguments. The supported keys are
            'id', 'size', 'x', and 'y'.
        """
        if len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Convert the square's attributes to a dictionary.

        Returns:
            dict: A dictionary containing the square's attributes
            - 'id', 'size', 'x', and 'y'.
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }
