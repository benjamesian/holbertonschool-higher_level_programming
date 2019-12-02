-- List number of records with same score
-- Ordered by number descending
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
