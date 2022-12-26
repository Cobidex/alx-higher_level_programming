#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name \
            FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(state_name)s \
            ORDER BY cities.id ASC""", {'state_name': sys.argv[4]})
    rows = c.fetchall()
    print(", ".join(row[1]) for row in rows)
    c.close()
    db.close()
