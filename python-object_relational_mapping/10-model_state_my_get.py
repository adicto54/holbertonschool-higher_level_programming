#!/usr/bin/python3
"""Prints the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1:5]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
