#!/usr/bin/python3

import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    mydb = sys.argv[3]
    

    engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{mydb}')
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()
    for state in states:
        if 'a' in state.name:
            session.delete(state)
    session.commit()
    session.close()
