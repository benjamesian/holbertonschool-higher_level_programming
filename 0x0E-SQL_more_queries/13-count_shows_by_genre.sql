-- List number of shows by genre
SELECT G.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres G
INNER JOIN tv_show_genres SG
ON SG.genre_id = G.id
GROUP BY SG.genre_id
ORDER BY number_of_shows DESC;
