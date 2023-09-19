#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(user=user, passwd=passwd, db=db_name, port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))
    cities = cur.fetchall()

    print(", ".join([city[0] for city in cities]))
