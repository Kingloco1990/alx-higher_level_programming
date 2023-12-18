#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get database credentials from command line arguments
    username, password, db_name = sys.argv[1:4]
    
    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and sort by states.id
    # .all() retrieves all the results as a list
    states = session.query(State).order_by(State.id).all()
    
    # Print all State objects
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
