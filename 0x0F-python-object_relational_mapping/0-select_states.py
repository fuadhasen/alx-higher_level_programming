#!/usr/bin/python3
import sys
import MySQLdb

mysql_usrs = sys.argv[1]
mysql_pwd = sys.argv[2]
db = sys.argv[3]

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', mysql_usrs, mysql_pwd, db)
    cursor = db.cursor()
    query = "SELECT * FROM `states`"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
