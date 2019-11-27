-- List all cities with states
SELECT C.id, C.name, S.name
FROM cities C, states S
WHERE C.state_id = S.id
ORDER BY C.id ASC;
