#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    # Connect to the MySQL server
    engine = (
            create_engine(
             f'mysql://{sys.argv[1]}:{sys.argv[2]}@\
             localhost:3306/{sys.argv[3]}')
            )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all cities sorted by id in ascending order
    cities = session.query(City).order_by(City.id).all()

    # Print the cities
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    # Close the session
    session.close()
