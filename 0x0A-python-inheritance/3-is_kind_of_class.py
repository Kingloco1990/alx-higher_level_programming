#!/usr/bin/python3
"""
Module containing the function `is_kind_of_class`,
which checks if an object is an instance or subclass of a given class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or subclass of a given class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The class to be checked against.

    Returns:
        bool: True if the object is an instance or subclass of the given
        class, False otherwise.
    """
    return isinstance(obj, a_class)
