SELECT COUNT(title) as Total
FROM movies
WHERE id in (
    SELECT movie_id
    FROM ratings
    WHERE rating = 10.0);

