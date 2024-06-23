#!/usr/bin/python3
""" script filter by state name """

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    mydb = sys.argv[3]
    if len(sys.argv) > 4:
        state_name = sys.argv[4]
    else:
        state_name = ''

    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{mydb}')
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name).first()
    if states is not None:
        print(f'{states.id}')
    else:
        print("Not found")
    session.close()
