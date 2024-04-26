#!/usr/bin/python3
"""This module filter  states from DB. """
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()

    cur.execute("""
        SELECT * FROM states
        where LEFT(name, 1) = "N"
        order by states.id
    """)
    res = cur.fetchall()
    for row in res:
        print(row)
