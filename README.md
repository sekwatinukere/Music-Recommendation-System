# 🎵 Music Recommendation System

**Python + MySQL + R + Spotify integration**

A portfolio-grade content-based music recommendation system.

## Important Spotify design decision

Spotify's current Web API documentation says Spotify Content may not be used to train a machine-learning or AI model. Therefore, this project trains its recommendation model on an independent/open music dataset and keeps Spotify as an optional catalog/user-integration layer.

## What this project demonstrates

- Python data cleaning and EDA
- Content-based recommendation
- Cosine similarity
- MySQL database design and SQL analytics
- R statistical analysis and regression
- Optional Spotify OAuth/catalog lookup
- Reproducible GitHub project structure

## Architecture

```text
Open Music Dataset
       ↓
Python ETL → MySQL
       ↓
Feature Engineering
       ↓
Content-Based Recommender
       ↓
Top-K Recommendations
       ├── R Statistical Analysis
       └── Optional Spotify Catalog Lookup
```

## Repository

```text
music-recommendation-system/
├── data/raw/tracks.csv
├── data/processed/
├── notebooks/01_music_recommendation_system.ipynb
├── python/spotify_catalog_lookup.py
├── src/data_pipeline.py
├── src/recommender.py
├── sql/database_schema.sql
├── sql/analytics_queries.sql
├── R/statistical_analysis.R
├── requirements.txt
└── README.md
```

## Dataset

The model expects:

`track_id, track_name, artist_name, genre, popularity, danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms`

The included CSV is a small generic demo dataset so the repository runs immediately. For the portfolio version, replace it with an independently licensed/open dataset such as the Million Song Dataset or another suitable music dataset.

**Do not train the model on Spotify API responses or Spotify Content.**

## Recommendation method

The baseline is content-based filtering:

1. Clean numeric audio/track features.
2. Standardise features with `StandardScaler`.
3. Calculate cosine similarity.
4. Given a seed track, return the most similar tracks.
5. Later evaluate Top-K recommendations with a held-out independent user-item dataset.

## MySQL

The database contains `tracks` and `listening_history`.

Example:

```sql
SELECT genre,
       COUNT(*) AS track_count,
       AVG(popularity) AS avg_popularity
FROM tracks
GROUP BY genre
ORDER BY avg_popularity DESC;
```

## R

R performs:

- descriptive statistics
- correlation analysis
- genre comparisons
- multiple linear regression

Example model:

```r
popularity ~ energy + danceability + valence + tempo + acousticness
```

## Spotify integration

The optional integration can authenticate a user and search Spotify's catalog to map a model-generated recommendation to a Spotify track/URL. It does not train the model on Spotify Content.

Use environment variables:

```text
SPOTIFY_CLIENT_ID
SPOTIFY_CLIENT_SECRET
SPOTIFY_REDIRECT_URI
```

Never commit credentials.

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/music-recommendation-system.git
cd music-recommendation-system
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Open `notebooks/01_music_recommendation_system.ipynb`.

## Future improvements

- hybrid recommendation
- collaborative filtering using an independent user-item dataset
- FastAPI backend
- Streamlit dashboard
- Docker
- automated tests
- cloud deployment
- recommendation explanations

## Portfolio skills

**Python:** pandas, NumPy, scikit-learn, EDA, feature engineering

**Machine Learning:** content-based recommendation, cosine similarity, ranking evaluation

**SQL:** relational schema, joins, aggregation, analytical queries

**R:** statistics, correlation, regression, ggplot2

**Engineering:** Git, environment variables, modular code, reproducibility
