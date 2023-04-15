#!/usr/bin/python3

"""
lists all states with a name starting with N
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port='3306')
    cur=db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == "N":
            print(row)

    cur.close()
    db.close()
