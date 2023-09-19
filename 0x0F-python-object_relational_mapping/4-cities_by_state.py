#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(user=user, passwd=passwd, db=db_name, port=3306)

    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM states \
        , cities WHERE states.id = cities.state_id;"
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)
