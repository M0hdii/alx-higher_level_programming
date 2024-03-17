#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(argv[0]))
        exit(1)

    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=mysql_username, passwd=mysql_password, db=database_name, port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))

