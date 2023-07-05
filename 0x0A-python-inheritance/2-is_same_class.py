#!/usr/bin/python3
"""
Module that provides a function that can be used to determine
if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Function that checks whether a given object is exactly
    and instance of a specified class.

    Args:
        obj: An object that needs to be checked.
        a_class: A class object or type to compare obj against.

    Returns:
        True if obj is exactly an instance of a_class.
        False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
