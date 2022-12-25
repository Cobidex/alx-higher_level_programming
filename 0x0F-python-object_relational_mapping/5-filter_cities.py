#!/usr/bin/python3

import sys
import MySQLdb

if "__name__" == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("
        SELECT c.name
        FROM states AS s
        INNER JOIN cities AS c
        ON s.id = c.state_id
        WHERE s.name = %s
        ORDER BY c.id ASC
    ", (sys.argv[4],))

    # Print results
    results = cursor.fetchall()
    if results:
        print(", ".join([result[0] for result in results]))

    # Close cursor and connection
    cursor.close()
    db.close()
