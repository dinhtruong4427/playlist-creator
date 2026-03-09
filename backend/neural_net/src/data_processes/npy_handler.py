from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 
import os

from neural_net.src.config.embedding_config import EMBEDDINGS_FILE_PATH

def get_item_index(item):
    item_array = np.load(EMBEDDINGS_FILE_PATH)
    
    # This calculates similarity for the whole database in one shot
    similarities = cosine_similarity(item.reshape(1, -1), item_array)[0]
    
    # Find the index of the highest similarity
    max_idx = np.argmax(similarities)
    
    # Check if the best match is actually "identical"
    if similarities[max_idx] >= 0.99999:
        print("This is the index of the song", int(max_idx))
        return int(max_idx)
        
    return None

def append_item(file_path, item):
    if os.path.exists(file_path):
        # Load and convert to a standard list
        data_list = np.load(file_path, allow_pickle=True).tolist()
    else:
        data_list = []

    # Direct append! No shapes, no axes, no dimensions.
    data_list.append(item)

    # Convert back to a NumPy array only for the save
    np.save(file_path, np.array(data_list))


    
