#!/usr/bin/python3
""" python script for state_fetch """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    mydb = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{mydb}',
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for state in states:
        print(f'{state.id}: {state.name}')
    session.close()
