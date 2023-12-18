#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City, Base
from model_state import State

if __name__ == '__main__':
    # Get database credentials from command line arguments
    username, password, db_name = sys.argv[1:4]

    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a Session class for interacting with the database
    Session = sessionmaker(bind=engine)

    # Establish a new session to execute queries
    session = Session()

    # Query for City objects and display the results
    cities = session.query(State, City).filter(State.id == City.state_id)\
                    .order_by(City.id).all()

    # Print the results
    for state, city in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # Close the session
    session.close()
