#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_update = session.query(State).filter(State.id == '2').first()
    state_update.name = "New Mexico"
    session.commit()

    session.close()
    engine.dispose()
