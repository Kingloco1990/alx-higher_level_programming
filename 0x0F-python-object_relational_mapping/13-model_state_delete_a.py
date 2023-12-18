#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get command line arguments
    username, password, db_name = sys.argv[1:4]

    # Create an engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query and delete all State objects with a name containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
