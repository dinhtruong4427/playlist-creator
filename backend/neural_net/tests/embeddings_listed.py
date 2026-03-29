import numpy as np

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH, PATHS_FILE_PATH

embeddings_list = np.load(EMBEDDINGS_FILE_PATH, allow_pickle=True).item()

#embeddings_dict = embeddings_list.item()

song_names = np.load(PATHS_FILE_PATH)

print("embeddings", embeddings_list.keys())
print("song names", song_names[-5:])

