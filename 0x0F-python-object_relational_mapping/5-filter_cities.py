#!/usr/bin/python3
"""python script sql injection free from hbtn_0e_0_usa database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_usrs = argv[1]
    mysql_pwd = argv[2]
    mydb = argv[3]
    if len(argv) > 4:
        state_name = argv[4]
    else:
        state_name = ''

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_usrs,
                         passwd=mysql_pwd,
                         db=mydb)

    cursor = db.cursor()
    query = """
            SELECT cities.name
            FROM cities
            LEFT JOIN states
            ON states.id = cities.state_id
            where states.name = %s
            ORDER BY cities.id
            """

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for index, row in enumerate(rows):
        if index < len(rows) - 1:
            print(row[0] + ', ', end='')
        else:
            print(row[0])
    print()
    cursor.close()
    db.close()
