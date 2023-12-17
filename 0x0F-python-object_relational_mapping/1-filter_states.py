#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Retrieve MySQL connection parameters from command-line arguments
    mysql_username, mysql_password, database_name = sys.argv[1:]

    # Connect to the MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query to retrieve states starting with 'N'
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")

    # Fetch all the results (rows)
    states = cur.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and database connection
    cur.close()
    db.close()
