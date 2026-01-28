-- dasdsda
USE hbtn_0d_usa;

SELECT *
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California' LIMIT 1)
ORDER BY id ASC;
