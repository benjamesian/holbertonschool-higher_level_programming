-- List all shows by rating
SELECT S.title, SUM(R.rate) AS rating
FROM tv_shows S
INNER JOIN tv_show_ratings R
ON S.id = R.show_id
GROUP BY S.title
ORDER BY rating DESC;
