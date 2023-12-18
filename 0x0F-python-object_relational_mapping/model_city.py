#!/usr/bin/python3
"""
Defines the City class and inherites from SQLAlchemy Base.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

# Create an instance of the declarative base class
Base = declarative_base()


# Define the State class, which inherits from Base
class City(Base):
    """
    Represents the City class corresponding to the 'cities' table
    in the database.

    Attributes:
        id (int): An auto-generated, unique integer serving as
        the primary key.

        name (str): A string column with a maximum length of 256 characters,
        cannot be null.

        state_id (int): An integer column representing the foreign key
        referencing the 'id' column in the 'states' table.
    """

    # Define the name of the corresponding database table
    __tablename__ = 'cities'

    # Define columns for the 'states' table
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    states_id = Column(Integer, ForeignKey('states.id'), nullable=False)
