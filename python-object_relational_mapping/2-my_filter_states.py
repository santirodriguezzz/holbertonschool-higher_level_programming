#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states"
                " WHERE BINARY name='{}'"
                " ORDER BY id ASC".format(sys.argv[4]))
    result = cursor.fetchall()
    for record in result:
        if record[1][0] == sys.argv[4]:
            print(record)
    cursor.close()
    db.close()
