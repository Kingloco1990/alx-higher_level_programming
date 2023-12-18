#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Database connection setup
    username, password, db_name = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query for State objects containing the letter 'a'
    states_with_a = session.query(State)\
        .filter(State.name.ilike('%a%'))\
        .order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print('{}: {}'.format(state.id, state.name))

    # Close the session
    session.close()
