#!/usr/bin/python3
"""
contains relationships codes
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the Base and State classes from the relationship_state module
from relationship_state import Base, State
# Import the City class from the relationship_city module
from relationship_city import City


if __name__ == "__main__":
    # Get the MySQL username, password, and database name from the comm
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

    # Create a new State object with the name "California"
    california = State(name="California")
    # Create a new City object with the name "San Francisco" and set it
    san_francisco = City(name="San Francisco", state=california)

    # Add the two objects to the session
    session.add(california)
    session.add(san_francisco)
    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
