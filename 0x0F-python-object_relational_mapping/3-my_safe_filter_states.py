#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

This script prevents SQL injections.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    # Connect to the MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query with user input as parameters
    # Use parameterized query to prevent SQL injection
    cur.execute("SELECT * FROM states \
        WHERE name = %s ORDER BY id", (sys.argv[4],))

    # Fetch all the results
    states = cur.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cur.close()
    db.close()
