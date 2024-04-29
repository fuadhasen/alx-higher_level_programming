#!/usr/bin/python3
"""This module update name state object using ORM """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user_name = sys.argv[1]
    user_passwd = sys.argv[2]
    user_DB = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user_name, user_passwd, user_DB),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    filter_users = session.query(State).filter(State.id == 2).all()

    filter_users[0].name = "New Mexico"
    session.commit()

    session.close()
