#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query to select all states
    cur.execute("SELECT * FROM states;")

    # Fetch all the rows
    states = cur.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()
