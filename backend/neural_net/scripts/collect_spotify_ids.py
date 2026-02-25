import csv
import time
from pathlib import Path
from tqdm import tqdm

from neural_net.src.clients.spotify import get_spotify_client

OUTPUT = Path("data/spotify_ids.csv")

YEARS = range(2000, 2026)
MARKETS = ["US", "GB", "DE", "FR", "JP", "BR", "IN", "KR"]

LIMIT = 50
SLEEP = 0.15  # rate limit safety

def load_existing_ids():
    if not OUTPUT.exists():
        return set()
    with open(OUTPUT) as f:
        return {row[0] for row in csv.reader(f)}

def save_ids(ids):
    with open(OUTPUT, "a", newline="") as f:
        writer = csv.writer(f)
        for tid in ids:
            writer.writerow([tid])

def main():
    sp = get_spotify_client()
    seen_ids = load_existing_ids()
    new_ids = set()

    for year in YEARS:
        for market in MARKETS:
            print(f"\nHarvesting year={year}, market={market}")

            offset = 0
            total_fetched = 0

            while offset < 10000:
                query = f"year:{year}"

                results = sp.search(
                    q=query,
                    type="track",
                    market=market,
                    limit=LIMIT,
                    offset=offset,
                )

                items = results["tracks"]["items"]
                if not items:
                    break

                for track in items:
                    tid = track.get("id")
                    if tid and tid not in seen_ids:
                        new_ids.add(tid)

                fetched = len(items)
                total_fetched += fetched
                offset += fetched

                time.sleep(SLEEP)

                if fetched < LIMIT:
                    break

            print(f"Fetched {total_fetched} results")

            if len(new_ids) >= 1000:
                save_ids(new_ids)
                seen_ids.update(new_ids)
                new_ids.clear()
                print("Checkpoint saved")

    if new_ids:
        save_ids(new_ids)

    print("Harvesting complete")

if __name__ == "__main__":
    main()
