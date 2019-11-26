-- List all genres by rating
SELECT G.name, SUM(R.rate) AS rating
FROM tv_genres G
LEFT JOIN tv_show_genres SG
ON G.id = SG.genre_id
INNER JOIN tv_show_ratings R
ON SG.show_id = R.show_id
GROUP BY G.name
ORDER BY rating DESC;
