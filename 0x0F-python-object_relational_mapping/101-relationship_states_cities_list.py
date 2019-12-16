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

    s = session.query(State)
    for state in s.all():
        print('{}: {}'.format(state.id, state.name))
        for c in state.cities:
            print('\t{}: {}'.format(c.id, c.name))
