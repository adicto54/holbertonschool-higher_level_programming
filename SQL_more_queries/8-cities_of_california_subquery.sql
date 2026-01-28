-- List all cities in California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California' LIMIT 1)
ORDER BY id ASC;
