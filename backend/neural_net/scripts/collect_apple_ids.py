import requests
import csv
import time
import string
from itertools import product

OUTPUT_CSV = "apple_tracks_v2.csv"
BASE_URL = "https://itunes.apple.com/search"

# max results per API call
LIMIT = 200

# generate search terms: single letters + double letters
def generate_search_terms():
    letters = string.ascii_lowercase
    terms = list(letters)  # a-z
    # double letters aa, ab, ac ... zz
    for combo in product(letters, repeat=2):
        terms.append("".join(combo))
    return terms

def collect_search_terms():
    terms = []
    with open("backend/neural_net/data/raw/song_discovery_terms.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            term = row["term"]
            terms.append(term)
    return terms

def fetch_tracks(term, limit=LIMIT):
    """
    Returns a list of tracks with previews for a search term.
    """
    params = {
        "term": term,
        "media": "music",
        "limit": limit
    }
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results", [])
        # only keep tracks with previewUrl
        tracks = [r for r in results if "previewUrl" in r]
        return tracks
    except Exception as e:
        print(f"Error fetching term '{term}': {e}")
        return []

def main():
    seen_ids = set()
    search_terms = collect_search_terms()
    print(f"Total search terms: {len(search_terms)}")

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["trackId", "trackName", "artistName", "albumArtwork", "previewUrl"])

        for term in search_terms:
            print(f"Searching term: {term}")
            tracks = fetch_tracks(term)
            for t in tracks:
                tid = t["trackId"]
                if tid not in seen_ids:
                    seen_ids.add(tid)
                    writer.writerow([
                        tid,
                        t.get("trackName", ""),
                        t.get("artistName", ""),
                        t.get("albumArtwork", ""),
                        t.get("previewUrl", "")
                    ])
            # polite pause to avoid hammering Apple API
            time.sleep(0.5)

    print(f"Finished! Total unique tracks collected: {len(seen_ids)}")
    print(f"Saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
