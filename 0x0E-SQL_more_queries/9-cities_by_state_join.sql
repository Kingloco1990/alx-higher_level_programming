-- Lists all cities contained in the database 'hbtn_0d_usa'.
-- The result of the script is ordered by ascending cities.id.
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
