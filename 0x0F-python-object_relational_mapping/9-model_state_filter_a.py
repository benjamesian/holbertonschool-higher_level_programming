#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    session = sessionmaker(bind=engine)()
    for state_id, name in session.query(
        State.id, State.name).filter(State.name.like('%a%'))\
            .order_by(State.id):
        print('{}: {}'.format(state_id, name))
