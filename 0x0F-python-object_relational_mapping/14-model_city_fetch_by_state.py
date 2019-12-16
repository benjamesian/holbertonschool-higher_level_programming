#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    session = sessionmaker(bind=engine)()
    q = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id)
    for c, s in q.all():
        print('{}: ({}) {}'.format(s.name, c.id, c.name))
    # session.commit()
