#!/usr/bin/python3
"""
Defines the State class and inherites from SQLAlchemy Base.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create an instance of the declarative base class
Base = declarative_base()


# Define the State class, which inherits from Base
class State(Base):
    """
    Represents the State class corresponding to the 'states' table
    in the database.

    Attributes:
        id (int): An auto-generated, unique integer serving as
        the primary key.

        name (str): A string column with a maximum length of 128 characters,
        cannot be null.
    """

    # Define the name of the corresponding database table
    __tablename__ = 'states'

    # Define columns for the 'states' table
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
