-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id, cities.name, state.name FROM cities, states
WHERE state.id = cities.id
ORDER BY cities.id ASC;
