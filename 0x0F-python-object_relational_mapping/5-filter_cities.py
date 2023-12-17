#!/usr/bin/python3
"""
Lists all cities of a specified state from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Connect to the MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    # Create a cursor object
    cur = db.cursor()

    # Execute the query to retrieve cities of the specified state
    cur.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id",
        (sys.argv[4],)
    )

    # Fetch all the results
    cities = cur.fetchall()

    # Display the results
    if cities:
        city_names = ', '.join(city[0] for city in cities)
        print(city_names)

    # Close the cursor and database connection
    cur.close()
    db.close()
