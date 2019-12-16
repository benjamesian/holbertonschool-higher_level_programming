#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    session = sessionmaker(bind=engine)()
    state = session.query(State)\
        .filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()
