-- List all cities with states
SELECT C.id, C.name AS name, S.name as name
FROM cities C
LEFT JOIN states S
ON S.id = C.state_id
ORDER BY C.id ASC;
