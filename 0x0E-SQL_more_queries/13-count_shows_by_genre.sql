-- Lists all genres from the database 'hbtn_0d_tvshows' along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.
SELECT t.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS t
INNER JOIN tv_show_genres AS g ON t.id = g.genre_id
GROUP BY t.name
ORDER BY number_of_shows DESC;
