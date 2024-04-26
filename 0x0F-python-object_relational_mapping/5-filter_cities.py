#!/usr/bin/python3
"""This module list all cities from DB. """
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
        Select cities.name
        From cities
        left join states
        on cities.state_id = states.id
        where states.name = %s
        order by cities.id
    """

    cur.execute(query, (statename,))
    res = cur.fetchall()
    for row in range(len(res)):
        city_name = res[row][0]
        if row < len(res) - 1:
            print(city_name, end=", ")
        else:
            print(city_name)
