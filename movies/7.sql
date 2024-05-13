SELECT m.title, r.rating
FROM movies m
JOIN ratings r on m.id = r.movie_id
where m.year = '2010'
ORDER BY r.rating DESC, m.title ASC;
