#!/usr/bin/python3
"""List all states with a name matching the argument hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor
    cur = conn.cursor()

    # Select all states with a name matching the argument, sorted by id
    query = f"SELECT * FROM states WHERE name={sys.argv[4]} ORDER BY id ASC"
    cur.execute(query)

    # Print the states
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
