import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

FEATURES = [
    "danceability", "energy", "loudness", "speechiness",
    "acousticness", "instrumentalness", "liveness",
    "valence", "tempo", "duration_ms"
]

class MusicRecommender:
    def __init__(self, data):
        self.data = data.copy()
        X = self.data[FEATURES].apply(pd.to_numeric, errors="coerce")
        X = X.fillna(X.median())
        self.matrix = StandardScaler().fit_transform(X)
        self.similarity = cosine_similarity(self.matrix)

    def recommend(self, seed_track_id, n=10):
        matches = self.data.index[
            self.data["track_id"].astype(str) == str(seed_track_id)
        ].tolist()

        if not matches:
            raise ValueError(f"Track ID not found: {seed_track_id}")

        idx = matches[0]
        ranked = sorted(
            enumerate(self.similarity[idx]),
            key=lambda x: x[1],
            reverse=True
        )

        output = []
        for i, score in ranked:
            if i == idx:
                continue
            row = self.data.iloc[i][
                ["track_id", "track_name", "artist_name", "genre"]
            ].copy()
            row["similarity"] = round(float(score), 4)
            output.append(row)
            if len(output) == n:
                break

        return pd.DataFrame(output)
