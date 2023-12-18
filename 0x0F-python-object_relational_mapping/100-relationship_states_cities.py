#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create California State and San Francisco City
    california = State(name='California', cities=[City(name='San Francisco')])
    session.add(california)
    session.commit()

    # Close the session
    session.close()
