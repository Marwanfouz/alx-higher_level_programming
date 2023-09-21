#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    citises = session.query(State, City).filter(State.id == City.state_id).all()

    for state, City in citises:
        print("{}: ({}) {}".format(state.name, City.id, City.name))
