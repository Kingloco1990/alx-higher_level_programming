#!/usr/bin/python3
"""This module contains a custom class, MyInt, which inherits from int."""


class MyInt(int):
    """
    A custom class that inherits from int and overrides
    comparison operators.
    """
    def __eq__(self, other):
        """
        Override the equality operator.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Override the inequality operator.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return not super().__ne__(other)
