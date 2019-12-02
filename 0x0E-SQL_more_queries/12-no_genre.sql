-- List all shows without a genre
SELECT S.title, G.genre_id
FROM tv_shows S
LEFT JOIN tv_show_genres G
ON S.id = G.show_id
WHERE G.genre_id IS NULL
ORDER BY S.title ASC, G.genre_id ASC;
