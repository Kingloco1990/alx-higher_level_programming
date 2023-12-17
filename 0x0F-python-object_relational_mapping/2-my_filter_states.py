#!/usr/bin/python3
'''
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
'''
import sys
import MySQLdb

if __name__ == '__main__':
    # Connect to the MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Prepare the SQL query using format with user input
    query = "SELECT * FROM states\
            WHERE BINARY name = '{}' ORDER BY id".format(sys.argv[4])

    # Execute the SQL query
    cur.execute(query)

    # Close the cursor and database connection
    cur.close()
    db.close()
