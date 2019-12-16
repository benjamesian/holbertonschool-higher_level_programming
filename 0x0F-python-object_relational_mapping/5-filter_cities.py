#!/usr/bin/python3
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    all_states = cur.execute("""
    SELECT c.name
    FROM cities c, states s
    WHERE c.state_id=s.id AND s.name=%s
    ORDER BY c.id ASC
    """, (argv[4],))
    city_names = ', '.join([el[0] for el in cur.fetchall()])
    print(city_names)
