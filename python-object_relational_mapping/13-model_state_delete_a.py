#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine to connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects containing the letter 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Loop through the results and delete each object
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction to save changes to the database
    session.commit()

    # Close the session
    session.close()