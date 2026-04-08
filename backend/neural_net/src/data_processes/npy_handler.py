from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import os

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH

def get_item_index(key):
    embeddings_dict = np.load(EMBEDDINGS_FILE_PATH, allow_pickle=True).item()
    song_ids = list(embeddings_dict.keys())
    embeddings = list(embeddings_dict.values())
    
    # This calculates similarity for the whole database in one shot
    index = song_ids.index(key)
    if index:
        return index
    return None


'''
This function is now adjusted for dictionaries
'''
def append_item(file_path, key, value):
    if os.path.exists(file_path):
        # Load and convert to a standard list
        data_dict = np.load(file_path, allow_pickle=True).item()
    else:
        data_dict = {}

    # Direct append! No shapes, no axes, no dimensions.
    data_dict[key] = value

    # Convert back to a NumPy array only for the save
    np.save(file_path, data_dict)


    
