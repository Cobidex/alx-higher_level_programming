#!/usr/bin/python3
"""
contains more relational scripts
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the Base and City classes from the relationship_state module
from relationship_state import Base, State
# Import the City class from the relationship_city module
from relationship_city import City

if __name__ == "__main__":
    # Get the MySQL username, password, and database name from the command-line arguments
    uname = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    # Create the connection string to the MySQL server
    link = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(link.format(uname, pwd, db))

    # Create a Session class to manage database interactions
    Session = sessionmaker(bind=engine)
    # Create a session instance
    session = Session()

    # Query the database for all City objects
    cities = session.query(City).order_by(City.id).all()

    # Iterate over the City objects and print their details
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
