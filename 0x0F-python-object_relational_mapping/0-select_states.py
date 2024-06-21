#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    mysql_usrs = sys.argv[1]
    mysql_pwd = sys.argv[2]
    mydb = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
            port=3306,
            user=mysql_usrs,
            passwd=mysql_pwd,
            db=mydb)

    cursor = db.cursor()
    query = "SELECT * FROM `states` ORDER BY states.id"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
