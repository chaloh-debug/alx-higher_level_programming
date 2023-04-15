#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

def state2cities():
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities INNER JOIN states \
                 ON states.id = cities.state_id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC;", [sys.argv[4]])
    rows = cur.fetchall()

    print(', '.join(map(lambda x: x[0], rows)))

    cur.close()
    db.close()


if __name__ == '__main__':
    state2cities()
