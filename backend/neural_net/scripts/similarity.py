import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH, PATHS_FILE_PATH, SONG_NUM
from neural_net.src.data_processes.npy_handler import get_item_index

# load embeddings file
embeddings_dict = np.load(EMBEDDINGS_FILE_PATH, allow_pickle=True).item()
song_ids = list(embeddings_dict.keys())
embeddings = list(embeddings_dict.values())

paths_dict = np.load(PATHS_FILE_PATH, allow_pickle=True).item()

#print(f"Loaded {embeddings.shape[0]} embeddings of dimension {embeddings.shape[1]}.")


def get_similar_songs_by_id(song_id, song_num=SONG_NUM):
    embeddings_dict = np.load(EMBEDDINGS_FILE_PATH, allow_pickle=True).item()
    song_ids = list(embeddings_dict.keys())
    embeddings = list(embeddings_dict.values())

    paths_dict = np.load(PATHS_FILE_PATH, allow_pickle=True).item()

    str_song_id = str(song_id)
    selected_song_index = get_item_index(str_song_id)

    print(f'This is the last item in python dict {list(paths_dict)[-1]}')
    print(f'Finding similar songs to {paths_dict[str_song_id]}')

    query_vector = embeddings_dict[str_song_id].reshape(1, -1)

    sims = cosine_similarity(query_vector, embeddings)[0]
    sims[selected_song_index] = -1

    top_indices = sims.argsort()[-song_num:][::-1]
    print("These are the indices of similar songs", top_indices)

    # Return list of (similarity_score, path)
    return [(sims[i], song_ids[i]) for i in top_indices]
'''
gets a given number of songs that are similar to a selected song

parameters:
query_index: index of the selected song
song_num: number of songs to be returned 

return:
- list of tuples (similarity score, file path)
'''
def get_similar_songs(query_index, song_num=SONG_NUM):
    embeddings_dict = np.load(EMBEDDINGS_FILE_PATH, allow_pickle=True).item()
    song_ids = list(embeddings_dict.keys())
    embeddings = list(embeddings_dict.values())

    paths_dict = np.load(PATHS_FILE_PATH, allow_pickle=True).item()
    # retrieves the vector of the selected song (note understand reshape)
    print(f"Finding similar songs to {paths_dict[query_index]}")

    query_vector = embeddings[query_index].reshape(1, -1)

    # computes cosine similarity (angle between 2 vectors) of all embeddings
    sims = cosine_similarity(query_vector, embeddings)[0]

    # removes the song itself as a potential option
    sims[query_index] = -1

    # returns the indexes of most similar songs based off cosine similarity
    top_indices = sims.argsort()[-song_num:][::-1]
    print("These are the indices of similar songs", top_indices)


    # Return list of (similarity_score, path)
    return [(sims[i], paths_dict[i]) for i in top_indices]

def get_similar_songs_by_embedding(query_embedding, song_num=SONG_NUM):
    embeddings_dict = np.load(EMBEDDINGS_FILE_PATH, allow_pickle=True).item()
    song_ids = list(embeddings_dict.keys())
    embeddings = list(embeddings_dict.values())

    paths_dict = np.load(PATHS_FILE_PATH, allow_pickle=True).item()
    # computes cosine similarity (angle between 2 vectors) of all embeddings
    sims = cosine_similarity(query_embedding.reshape(1, -1), embeddings)[0]

    # returns the indexes of most similar songs based off cosine similarity
    top_indices = sims.argsort()[-song_num:][::-1]

    # Return list of (similarity_score, path)
    return [(sims[i], paths_dict[i]) for i in top_indices]

if __name__ == "__main__":
    query_idx = '1418213392'
    print("This is the similar song", paths_dict)
    similar_songs = get_similar_songs_by_id(query_idx, song_num=SONG_NUM)

    print(f"\nTop {SONG_NUM} songs similar to:\n{paths_dict[query_idx]}\n")
    for score, song_id in similar_songs:
        print(f"{score:.4f} → {paths_dict[song_id]}")
