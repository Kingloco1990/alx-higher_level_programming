#!/usr/bin/python3
"""
Module to determine if an object is an instance of a class that
directly or indirectly inherits from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that directly
    or indirectly inherits from the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to check against.

    Returns:
        bool: True if the object is an instance of a
        class that inherits from the specified class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
