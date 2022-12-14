#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""

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

    new_obj = State(name='Louisiana')
    session.add(new_obj)
    session.commit()
    print(new_obj.id)
    session.close()
