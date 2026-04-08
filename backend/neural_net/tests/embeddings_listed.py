import numpy as np

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH, PATHS_FILE_PATH

embeddings_list = np.load(EMBEDDINGS_FILE_PATH, allow_pickle=True).item()

#embeddings_dict = embeddings_list.item()

song_names = np.load(PATHS_FILE_PATH, allow_pickle=True).item()

print("embeddings", list(embeddings_list.keys()), type(list(embeddings_list.keys())[0]))
print("song names", list(song_names.values()))

