-- List genres of Dexter
SELECT G.name
FROM tv_shows S
INNER JOIN tv_show_genres SG
ON S.id = SG.show_id
INNER JOIN tv_genres G
ON G.id = SG.genre_id
WHERE S.title = "Dexter"
ORDER BY G.name ASC;
