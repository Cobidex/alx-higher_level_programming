#!/usr/bin/python3
"""print first State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    u_name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(u_name, pwd, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(State.id).first()
    if data is None:
        print('Nothing')
    else:
        print('{}: {}'. format(data.id, data.name))

    session.close()
