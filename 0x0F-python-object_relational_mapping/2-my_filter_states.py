#!/usr/bin/python3
"""python script that filter by user input from hbtn_0e_0_usa database"""
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
            SELECT * FROM `states`
            WHERE name = '{}'
            ORDER BY states.id
            """.format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()

