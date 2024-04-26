#!/usr/bin/python3
"""This module list all cities of specified state from DB. """
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
        SELECT cities.name
        FROM cities
        left join states
        on cities.state_id = states.id
        where states.name = %s
        order by cities.id
    """

    cur.execute(query, (statename,))
    res = cur.fetchall()
    for row in res:
        city_name = row[0]
        print(city_name, end=", ")
    print()
