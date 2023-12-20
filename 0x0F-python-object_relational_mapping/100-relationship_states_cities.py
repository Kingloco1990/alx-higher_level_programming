#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
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

    # Create State "California" with City "San Francisco"
    california = State(name='California', cities=[City(name='San Francisco')])

    # Add the State to the session and commit change
    session.add(california)
    session.commit()

    # Close the session
    session.close()
