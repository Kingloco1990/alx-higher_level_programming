#!/usr/bin/python3
"""This module defines the BaseGeometry class for geometric calculations."""


class BaseGeometry:
    """A base class for geometric calculations."""
    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.

        Returns:
            None
        """
        raise Exception("area() is not implemented")
