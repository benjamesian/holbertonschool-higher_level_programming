-- Select all records where score is at least 10
-- Records ordered by score, only score and name selected
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
