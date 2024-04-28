#!/usr/bin/python3
"""This module list all states from DB. """
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

    cur.execute('SELECT * FROM states order by states.id')
    res = cur.fetchall()
    for row in res:
        print(row)