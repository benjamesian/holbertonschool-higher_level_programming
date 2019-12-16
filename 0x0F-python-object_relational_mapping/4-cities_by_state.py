#!/usr/bin/python3
import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    all_states = cur.execute("""
    SELECT c.id, c.name, s.name
    FROM cities c, states s
    WHERE c.state_id=s.id
    ORDER BY c.id ASC
    """)
    for record in cur.fetchall():
        print(record)
