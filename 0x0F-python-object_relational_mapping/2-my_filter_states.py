#!/usr/bin/python3
"""
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=hbtn_0e_0_usa, name=sys.argv[4], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * \
            FROM states \
            WHERE name LIKE '{}'".format(sys.argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
