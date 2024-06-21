#!/usr/bin/python3
import sys
import MySQLdb

mysql_usrs = sys.argv[1]
mysql_pwd = sys.argv[2]
mydb = sys.argv[3]

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=mysql_usrs, passwd=mysql_pwd, db=mydb)
    cursor = db.cursor()
    query = "SELECT * FROM `states`"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
