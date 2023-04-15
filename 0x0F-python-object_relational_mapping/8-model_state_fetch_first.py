#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
             sys.argv[1], sys.argv[2], sys.argv[3], port=3306),
             pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    session.close()
    engine.destroy()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
