import numpy as np 
import os

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH

def get_embedding_index(embedding):
    embedding_array = np.load(EMBEDDINGS_FILE_PATH)

    for index, current_embedding in enumerate(embedding_array):
        if current_embedding == embedding[0]:
            print(f"Found same embedding at index {index}: {current_embedding}")
            return index

def append_embedding(file_path, embedding):
    if os.path.exists(file_path):
        # Load the existing array
        existing_data = np.load(file_path, allow_pickle=True)
        # Combine them (assuming you're adding a row)
        updated_data = np.vstack((existing_data, embedding))
    else:
        # If file doesn't exist, start fresh
        updated_data = file_path

    np.save(file_path, updated_data)


    
