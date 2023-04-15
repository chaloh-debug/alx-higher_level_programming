#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    un = sys.argv[1]
    passd = sys.argv[2]
    datab = sys.argv[3]
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             un, passd, port, datab), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    session.close()
    engine.dispose()

    for state in states:
        print("{}: {}".format(state.id, state.name))
