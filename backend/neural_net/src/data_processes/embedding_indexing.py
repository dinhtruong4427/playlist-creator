import numpy as np 

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH

def get_embedding_index(embedding):
    embedding_array = np.load(EMBEDDINGS_FILE_PATH)

    for index, current_embedding in enumerate(embedding_array):
        if current_embedding[0] == embedding:
            print(f"Found same embedding at index {index}: {current_embedding}")
            return index


    
