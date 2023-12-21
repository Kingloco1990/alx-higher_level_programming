#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == '__main__':
    # Get database credentials from command line arguments
    username, password, db_name = sys.argv[1:4]

    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create tables based on defined metadata for the specified database engine
    Base.metadata.create_all(engine)

    # Create a Session class for interacting with the database
    Session = sessionmaker(bind=engine)

    # Establish a new session to execute queries
    session = Session()

    # Query for all City objects with related State, sorted by cities.id
    cities_states = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities_states:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
