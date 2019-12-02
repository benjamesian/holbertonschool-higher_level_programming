-- Shows that are not Comedy
SELECT title
FROM tv_shows
WHERE id NOT IN
      (SELECT S.id
      FROM tv_shows S
      INNER JOIN tv_show_genres SG
      ON S.id = SG.show_id
      INNER JOIN tv_genres G
      ON SG.genre_id = G.id
      WHERE G.name = "Comedy")
ORDER BY title ASC;
