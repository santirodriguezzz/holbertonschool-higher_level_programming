#!/usr/bin/python3
"""script that lists all states with a name starting with N from the database hbtn_0e_0_usa"""
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;")
    result = cursor.fetchall()
    for record in result:
        if record[1][0] == 'N':
            print(record)
    cursor.close()
    db.close()
