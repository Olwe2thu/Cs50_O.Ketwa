SELECT  p.name
FROM  people p
JOIN stars s on p.id = s.person_id
JOIN movies m on m.id = s.movie_id
WHERE m.title = 'Toy Story';
