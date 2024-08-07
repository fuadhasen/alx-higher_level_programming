#!/usr/bin/python3
"""python script  cities_by_state from hbtn_0e_0_usa database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_usrs = argv[1]
    mysql_pwd = argv[2]
    mydb = argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_usrs,
                         passwd=mysql_pwd,
                         db=mydb)

    cursor = db.cursor()
    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            LEFT JOIN states
            ON states.id = cities.state_id
            ORDER BY cities.id
            """

    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
