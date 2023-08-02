#!/usr/bin/python3
"""
This module provides a Base class which will serve as the "base"
of all other classes in this project (0x0C. Python - Almost a circle).
"""
import json
import csv
import turtle


class Base:
    """
    Represents the Base class

    Attributes:
        __nb_objects (int): A private class variable to track the
        number of Base objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object with a unique identifier.

        Args:
            id (int, optional): The identifier for the object.
            Defaults to None, in which case a new identifier is assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serializes a list of dictionaries to a JSON formatted string.

        Args:
            list_dictionaries (List[dict]): A list of dictionaries to be
            serialized.

        Returns:
            str: A JSON formatted string representing the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (List[Base]): A list of Base objects to be saved to the
            file.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as j_file:
            if list_objs is None:
                j_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                j_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Deserializes a JSON formatted string to a list of dictionaries.

        Args:
            json_string (str): A JSON formatted string.

        Returns:
            List[dict]: A list of dictionaries representing the JSON data
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance of the class from a dictionary of attributes.

        Args:
            **dictionary (dict): Keyword arguments representing the attributes
            of the object.

        Returns:
            Base: An instance of the class with the specified attributes.

        """
        if dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Load objects from a JSON file.

        Returns:
            List[Base]: A list of Base objects loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as j_file:
                list_dicts = Base.from_json_string(j_file.read())
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of objects to a CSV file.

        Args:
            list_objs (List[Base]): A list of Base objects to be saved to the
            file.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as c_file:
            if list_objs is None or list_objs == []:
                c_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(c_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads objects from a CSV file.

        Returns:
            List[Base]: A list of Base objects loaded from the file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as c_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(c_file, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws a visualization of the given list of rectangles and squares using
        Turtle graphics.

        Args:
            list_rectangles (List[Rectangle]): A list of Rectangle objects to
            be drawn.
            list_squares (List[Square]): A list of Square objects to be drawn.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
