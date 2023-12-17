#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Connect to the MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query to retrieve all cities with state information
    cur.execute(
        "SELECT cities.id, cities.name, states.name"
        "FROM cities"
        "JOIN states ON cities.state_id = states.id"
        "ORDER BY cities.id"
    )

    # Fetch all the results
    cities = cur.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cur.close()
    db.close()
