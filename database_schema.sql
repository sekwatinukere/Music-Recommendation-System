CREATE DATABASE IF NOT EXISTS music_recommendation;
USE music_recommendation;

CREATE TABLE IF NOT EXISTS tracks (
    track_id VARCHAR(100) PRIMARY KEY,
    track_name VARCHAR(255) NOT NULL,
    artist_name VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    popularity FLOAT,
    danceability FLOAT,
    energy FLOAT,
    loudness FLOAT,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness FLOAT,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    duration_ms INT
);

CREATE TABLE IF NOT EXISTS listening_history (
    history_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(100) NOT NULL,
    track_id VARCHAR(100) NOT NULL,
    played_at DATETIME,
    rating FLOAT,
    FOREIGN KEY (track_id) REFERENCES tracks(track_id)
);
