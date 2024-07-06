#!/usr/bin/python3
"""script for model_city_fetch """

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    from model_city import Base, City
    from model_state import Base, State

    user = sys.argv[1]
    pwd = sys.argv[2]
    mydb = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{mydb}')
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State, City).filter(State.id == City.state_id)
    res.order_by(City.id)
    for state, city in res:
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
