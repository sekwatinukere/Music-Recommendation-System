import pandas as pd
from pathlib import Path

RAW = Path("data/raw/tracks.csv")
PROCESSED = Path("data/processed/cleaned_tracks.csv")

def clean_music_data():
    df = pd.read_csv(RAW).drop_duplicates(subset=["track_id"]).copy()

    numeric = [
        "popularity", "danceability", "energy", "loudness",
        "speechiness", "acousticness", "instrumentalness",
        "liveness", "valence", "tempo", "duration_ms"
    ]

    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

    df["genre"] = df["genre"].fillna("Unknown")
    df["artist_name"] = df["artist_name"].fillna("Unknown Artist")
    df["track_name"] = df["track_name"].fillna("Unknown Track")

    PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED, index=False)
    return df

if __name__ == "__main__":
    clean_music_data()
    print(f"Saved cleaned data to {PROCESSED}")
