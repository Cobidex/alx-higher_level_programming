#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    link = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(link. format(uname, pwd, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print('{}: ({}) {}'. format(city.state.name, city.id, city.name))

    session.close()
