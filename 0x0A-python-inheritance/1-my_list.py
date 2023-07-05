#!/usr/bin/python3
"""Module containing the MyList class, a custom list implementation."""


class MyList(list):
    """MyList class that extends the built-in list class."""
    def print_sorted(self):
        """Function that prints the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
