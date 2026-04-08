import requests

from neural_net.scripts.similarity import get_similar_songs, get_similar_songs_by_embedding, get_similar_songs_by_id
from neural_net.scripts.extract_yamnet_embeddings import apple_single_embedding_extraction
from neural_net.src.data_processes.npy_handler import get_item_index

def find_similar_songs(song_id, top_n=5):
    similar_songs_array = []
    #cleaned_song_url = song_url.replace("https://", "http://")


    selected_song = get_song_by_id(song_id)

    song_url = selected_song["previewUrl"]
    song_url = song_url.replace("https://", "http://")

    song_name = selected_song["title"]

    apple_single_embedding_extraction(song_id, song_url, song_name)


    similar_songs = get_similar_songs_by_id(song_id, top_n)

    '''
    reverted so it works
    query_index = get_item_index(embedding)

    similar_songs = get_similar_songs(query_index, song_num=top_n)
    '''

    for score, path in similar_songs:
        current_song = get_song_by_id(int(path))
        if current_song:
            similar_songs_array.append(current_song)

    
    return similar_songs_array

def get_song_by_id(track_id: int):
    """
    Retrieve a song object from an Apple trackId using the public iTunes API.
    """
    ITUNES_LOOKUP_URL = "https://itunes.apple.com/lookup"
    params = {
        "id": track_id,
        "entity": "song"
    }

    resp = requests.get(ITUNES_LOOKUP_URL, params=params, timeout=10)
    resp.raise_for_status()

    data = resp.json()
    results = data.get("results", [])

    if not results:
        return None

    track = results[0]

    return {
        "id": track.get("trackId"),
        "title": track.get("trackName"),
        "artist": track.get("artistName"),
        "albumArtwork": track.get("artworkUrl100"),
        "previewUrl": track.get("previewUrl")
    }