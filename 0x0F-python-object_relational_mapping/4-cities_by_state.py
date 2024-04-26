#!/usr/bin/python3
"""This module list all cities from DB. """
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
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        left join states
        on cities.state_id = states.id
        order by cities.id
    """

    cur.execute(query)
    res = cur.fetchall()
    for row in res:
        print(row)
