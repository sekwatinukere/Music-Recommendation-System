import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SCOPES = "user-top-read user-read-recently-played"

def spotify_client():
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
            scope=SCOPES,
        )
    )

def search_catalog(sp, track_name, artist_name, limit=5):
    query = f"track:{track_name} artist:{artist_name}"
    results = sp.search(q=query, type="track", limit=limit)

    return [
        {
            "name": item["name"],
            "artist": ", ".join(a["name"] for a in item["artists"]),
            "spotify_id": item["id"],
            "spotify_url": item["external_urls"].get("spotify"),
        }
        for item in results["tracks"]["items"]
    ]
