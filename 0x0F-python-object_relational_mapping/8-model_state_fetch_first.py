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

    Session = sessionmaker(bind=engine)
    session = Session()
    first_usr = session.query(State).first()

    if not first_usr:
        print()
    else:
        print("{}: {}".format(first_usr.id, first_usr.name))

    session.close()
