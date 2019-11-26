-- List all cities with states
SELECT C.id, C.name AS name, S.name as name
FROM states S
INNER JOIN cities C
ON S.id = C.state_id
ORDER BY C.id ASC;
