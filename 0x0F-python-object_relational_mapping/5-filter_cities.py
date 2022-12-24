#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""


import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # Prepare the SELECT statement with placeholders
    query = "SELECT cities.name \
            FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"

    # Execute the SELECT statement
    cursor.execute(query, (sys.argv[4],))

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row[0])
