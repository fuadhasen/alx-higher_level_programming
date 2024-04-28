#!/usr/bin/python3
"""This module list first state objcet using ORM """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user_name = sys.argv[1]
    user_passwd = sys.argv[2]
    user_DB = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user_name, user_passwd, user_DB
    ))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    filter_users = session.query(State).limit(1).all()

    if not filter_users:
        print()
    else:
        for state in filter_users:
            print("{}: {}".format(state.id, state.name))

    session.close()
