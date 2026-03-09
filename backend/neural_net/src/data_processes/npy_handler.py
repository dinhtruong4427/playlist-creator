import numpy as np 
import os

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH

def get_item_index(item):
    item_array = np.load(EMBEDDINGS_FILE_PATH)

    for index, current_item in enumerate(item_array):
        if current_item == item:
            print(f"Found same embedding at index {index}: {current_item}")
            return index
    
    return None

def append_item(file_path, item):
    if os.path.exists(file_path):

        existing_data = np.load(file_path, allow_pickle=True)

        updated_data = np.vstack((existing_data, item))
    else:
        updated_data = file_path

    np.save(file_path, updated_data)


    
