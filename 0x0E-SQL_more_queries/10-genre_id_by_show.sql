-- List all shows that have a genre linked
SELECT S.title AS title, G.genre_id
FROM tv_shows S
INNER JOIN tv_show_genres G
ON S.id = G.show_id
ORDER BY S.title ASC, G.genre_id ASC;
