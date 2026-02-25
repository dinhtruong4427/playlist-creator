# app/services/search.py
from typing import List, Dict
import requests

# Dummy dataset for now

BASE_URL = "https://itunes.apple.com/search"

def search_songs(query: str):
    """
    Return a list of songs that match the query in title or artist.
    """
    params = {
        "term": query,
        "media": "music",
        "limit": 5
    }
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results", [])
        # only keep tracks with previewUrl
        tracks = [r for r in results if "previewUrl" in r]
        returned_tracks = []
        for track in tracks:
            returned_tracks.append({
                "id": track.get("trackId"),
                "title": track.get("trackName"),
                "artist": track.get("artistName"),
                "albumArtwork": track.get("artworkUrl100"),
                "previewUrl": track.get("previewUrl")
            })
        return returned_tracks
    except Exception as e:
        print(f"Error fetching term '{query}': {e}")
        return []
