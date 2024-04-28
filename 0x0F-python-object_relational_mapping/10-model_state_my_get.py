#!/usr/bin/python3
"""This module search state objcet using ORM """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user_name = sys.argv[1]
    user_passwd = sys.argv[2]
    user_DB = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user_name, user_passwd, user_DB),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    filter_users = session.query(State).filter(State.name == state_name).all()

    if not filter_users:
        print("Not found")
    else:
        for state in filter_users:
             print("{}".format(state.id))

    session.close()
