import numpy as np

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH, PATHS_FILE_PATH

embeddings_list = np.load(EMBEDDINGS_FILE_PATH).item()
song_names = np.load(PATHS_FILE_PATH)

print("embeddings", embeddings_list[-5:])
print("song names", song_names[-5:])

