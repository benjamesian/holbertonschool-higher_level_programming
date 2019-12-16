#!/usr/bin/python3
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    city = City(name="San Francisco")
    state = State(name="California")
    state.cities.extend([city])
    session.add(state)
    session.add(city)
    session.commit()
