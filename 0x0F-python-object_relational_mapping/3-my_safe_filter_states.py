#!/usr/bin/python3
"""
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
with adjustment to prevent sql injection.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(user=user, passwd=passwd, db=db_name, port=3306)

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s;"
    cur.execute(query, (state_name,))
    states = cur.fetchall()

    for state in states:
        print(state)
