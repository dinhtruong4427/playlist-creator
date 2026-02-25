import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH, PATHS_FILE_PATH, SONG_NUM

# load embeddings file
embeddings = np.load(EMBEDDINGS_FILE_PATH)
paths = np.load(PATHS_FILE_PATH)

print(f"Loaded {embeddings.shape[0]} embeddings of dimension {embeddings.shape[1]}.")

'''
gets a given number of songs that are similar to a selected song

parameters:
query_index: index of the selected song
song_num: number of songs to be returned 

return:
- list of tuples (similarity score, file path)
'''
def get_similar_songs(query_index, song_num=SONG_NUM):
    # retrieves the vector of the selected song (note understand reshape)
    query_vector = embeddings[query_index].reshape(1, -1)

    # computes cosine similarity (angle between 2 vectors) of all embeddings
    sims = cosine_similarity(query_vector, embeddings)[0]

    # removes the song itself as a potential option
    sims[query_index] = -1

    # returns the indexes of most similar songs based off cosine similarity
    top_indices = sims.argsort()[-song_num:][::-1]

    # Return list of (similarity_score, path)
    return [(sims[i], paths[i]) for i in top_indices]

def get_similar_songs_by_embedding(query_embedding, song_num=SONG_NUM):
    # computes cosine similarity (angle between 2 vectors) of all embeddings
    sims = cosine_similarity(query_embedding.reshape(1, -1), embeddings)[0]

    # returns the indexes of most similar songs based off cosine similarity
    top_indices = sims.argsort()[-song_num:][::-1]

    # Return list of (similarity_score, path)
    return [(sims[i], paths[i]) for i in top_indices]

if __name__ == "__main__":
    query_idx = 100
    similar_songs = get_similar_songs(query_idx, song_num=SONG_NUM)

    print(f"\nTop {SONG_NUM} songs similar to:\n{paths[query_idx]}\n")
    for score, path in similar_songs:
        print(f"{score:.4f} → {path}")
