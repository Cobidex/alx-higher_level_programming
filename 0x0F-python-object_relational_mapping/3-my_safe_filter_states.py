#!/usr/bin/python3
"""takes in arguments and displays all values"""


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

    # Use a parameterized query to protect against MySQL injection attacks
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)
