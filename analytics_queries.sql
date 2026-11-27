USE music_recommendation;

SELECT genre, COUNT(*) AS track_count,
       ROUND(AVG(popularity),2) AS avg_popularity
FROM tracks
GROUP BY genre
ORDER BY avg_popularity DESC;

SELECT genre, ROUND(AVG(energy),3) AS avg_energy
FROM tracks
GROUP BY genre
ORDER BY avg_energy DESC;

SELECT artist_name, COUNT(*) AS tracks,
       ROUND(AVG(popularity),2) AS avg_popularity
FROM tracks
GROUP BY artist_name
HAVING COUNT(*) >= 2
ORDER BY avg_popularity DESC
LIMIT 20;

SELECT user_id, COUNT(*) AS plays,
       ROUND(AVG(rating),2) AS avg_rating
FROM listening_history
GROUP BY user_id
ORDER BY plays DESC;
