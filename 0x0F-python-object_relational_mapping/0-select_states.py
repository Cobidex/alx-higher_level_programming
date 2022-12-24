#!/usr/bin/python3
"""Lists all states from the database hbtn0e_0_usa"""


import sys
import MySQLdb

# connect to MySQL server
con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

# create a cursor
cursor = con.cursor()

# Select all states from the states table, sorted by id
querry = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(querry)

# print all states
states = cursor.fetchall()
for state in states:
    print(state)

# close cursor and connection
cursor.close()
con.close()
