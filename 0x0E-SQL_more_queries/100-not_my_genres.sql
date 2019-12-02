-- List all genres not linked to Dexter
SELECT name
FROM tv_genres
WHERE name NOT IN
      (SELECT G.name
      FROM tv_genres G
      INNER JOIN tv_show_genres SG
      ON G.id = SG.genre_id
      LEFT JOIN tv_shows S
      ON SG.show_id = S.id
      WHERE S.title = "Dexter")
ORDER BY name ASC;
