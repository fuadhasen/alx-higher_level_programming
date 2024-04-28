#!/usr/bin/python3
"""This module list all state objcet using ORM """


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    user_name = sys.argv[1]
    user_passwd = sys.argv[2]
    user_DB = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user_name, user_passwd, user_DB
    ))

    Session = sessionmaker(bind=engine)
    session = Session()
    filter_users = session.query(State).order_by(State.id).all()

    for state in filter_users:
        flag = False
        for char in state.name:
            if char == 'a':
                flag = True
                break
        if flag is True:
            print("{}: {}".format(state.id, state.name))

    session.close()