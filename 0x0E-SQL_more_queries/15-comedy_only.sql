-- Lists all comedy shows in the database 'hbtn_0d_tvshows'.
-- Records are ordered by descending show title.
SELECT t.title
FROM tv_shows AS t
INNER JOIN tv_show_genres AS s ON t.id = s.show_id
INNER JOIN tv_genres AS g ON s.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY t.title;
