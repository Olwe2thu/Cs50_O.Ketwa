SELECT DISTINCT p.name
FROM stars s1
JOIN stars s2 ON s1.movie_id = s2.movie_id
JOIN people p ON s1.person_id = p.id
JOIN people kevin ON s2.person_id = kevin.id
WHERE kevin.name = 'Kevin Bacon' AND kevin.birth = 1958
    AND p.name != 'Kevin Bacon';

