#!/usr/bin/python3
"""
This module provides a class called Student for representing student objects.
"""
import os
import sys


class Student:
    """
    Represents a student with first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the student object to a JSON-compatible dictionary.

        Args:
            attrs (list, optional): A list of attributes to include in the
                                    JSON representation. Defaults to None.

        Returns:
            dict: A dictionary representing the student object in JSON format.
                If `attrs` is specified, only the specified attributes will be
                included.
                If `attrs` is None, all attributes will be included.
        """
        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            json_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    json_dict[attr] = self.__dict__[attr]
            return json_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        Reloads the student object from a JSON dictionary.

        Args:
            json (dict): A dictionary representing the student object
            in JSON format. It should contain the keys
            'first_name', 'last_name', and 'age'.
        """
        for key, value in json.items():
            setattr(self, key, value)
