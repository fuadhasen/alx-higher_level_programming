#!/usr/bin/python3
"""This module search states from DB. """
import sys
import MySQLdb


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    query = """
        SELECT * FROM states
        where name = %s
        order by states.id
    """

    cur.execute(query, (statename,))
    res = cur.fetchall()
    for row in res:
        print(row)
