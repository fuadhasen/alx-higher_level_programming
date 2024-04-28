#!/usr/bin/python3
""" Changes the name of a State object from DB """

if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    user = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    url = f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db_name}"

    engine = create_engine(url)

    Session = sessionmaker(bind=engine)
    session = Session()

    changed_state = session.query(State).filter(State.id == 2).one()

    changed_state.name = "New Mexico"

    session.commit()
    session.close()
