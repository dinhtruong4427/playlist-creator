# package imports
import os
import numpy as np
from tqdm import tqdm

# file imports
from neural_net.src.data_processes.audio_indexing import collect_audio_files, collect_apple_samples
from neural_net.src.data_processes.audio_loader import load_audio, load_apple_audio
from neural_net.src.data_processes.npy_handler import append_item
# from backend.neural_net.src.data_processes.batch_builder import build_apple_batches
from neural_net.src.models.yamnet_embedder import YAMNetEmbedder
from neural_net.src.config.embedding_config import APPLE_ROOT, AUDIO_ROOT, OUTPUT_DIR, DURATION, SAMPLE_RATE

def local_embedding_extraction():
    # verifies if the output exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # collect audio files
    audio_files = collect_audio_files(AUDIO_ROOT)
    print(f"Found {len(audio_files)} audio files")

    # set embedding
    embedder = YAMNetEmbedder()
    embeddings = []
    paths = []

    for path in tqdm(audio_files, desc="Processing Ding's audio files"):
        try:
            # load audio file from path
            audio, sr = load_audio(path, sr=SAMPLE_RATE, duration=DURATION)

            # converts audio into vectors and embeds into model
            emb = embedder.embed(audio, sr)

            # adds embedding and path
            embeddings.append(emb)
            paths.append(path)

        except Exception as e:
            print(f"Skipping {path}: {e}")

    # convert list of embeddings to a single matrix
    embeddings = np.stack(embeddings)

    # save outputs
    np.save(os.path.join(OUTPUT_DIR, "yamnet_embeddings.npy"), embeddings)
    np.save(os.path.join(OUTPUT_DIR, "paths.npy"), paths)

    print(f"Saved {len(embeddings)} embeddings to {OUTPUT_DIR}")

def apple_embedding_extraction():
    # verifies if the output exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # collect audio files
    audio_files = collect_apple_samples(APPLE_ROOT)
    print(f"Found {len(audio_files)} apple urls")

    # set embedding
    embedder = YAMNetEmbedder()
    embeddings = {}
    paths = {}

    # song_obj = (previewUrl, trackId, trackName)
    for song_obj in tqdm(audio_files, desc="Processing Ding's apple audio files"):
        try:
            # load audio file from path
            audio, sr = load_apple_audio(song_obj[0], sr=SAMPLE_RATE, duration=DURATION)

            # converts audio into vectors and embeds into model
            emb = embedder.embed(audio, sr)

            # adds embedding and path
            embeddings[song_obj[1]] = emb
            paths[song_obj[1]] = song_obj[2]

        except Exception as e:
            print(f"Skipping {song_obj[1]}: {e}")

    # convert list of embeddings to a single matrix

    #embeddings = np.stack(embeddings)
    #paths = np.stack(paths)

    # save outputs
    np.save(os.path.join(OUTPUT_DIR, "yamnet_apple_embeddings_v2.npy"), embeddings)
    np.save(os.path.join(OUTPUT_DIR, "apple_song_names.npy"), paths)

    print(f"Saved {len(embeddings)} embeddings to {OUTPUT_DIR}")


'''
Shut down temporarily due to lack of batching support

def apple_batched_embedding_extraction():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    audio_files = collect_apple_samples(APPLE_ROOT)
    print(f"Found {len(audio_files)} apple urls")

    embedder = YAMNetEmbedder()
    embedding_list = []
    song_names = []
    batch_count = 0

    for audio_batch, names in build_apple_batches(audio_files):
        batch_count += 1
        print(f"Processing batch {batch_count}, size {len(audio_batch)}")

        batch_embeddings = embedder.embed_batch(audio_batch)

        for emb, name in zip(batch_embeddings, names):
            embedding_list.append(emb)
            song_names.append(name)

    # convert list of embeddings to a single matrix
    embeddings = np.stack(embedding_list)

    # save outputs
    np.save(os.path.join(OUTPUT_DIR, "yamnet_apple_batched_embeddings.npy"), embeddings)
    np.save(os.path.join(OUTPUT_DIR, "apple_song_names.npy"), song_names)

    print(f"Saved {len(embeddings)} embeddings to {OUTPUT_DIR}")
'''

def apple_single_embedding_extraction(song_id, song_url, song_name):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    embedder = YAMNetEmbedder()

    audio, sr = load_apple_audio(song_url, sr=SAMPLE_RATE, duration=DURATION)

    embedding = embedder.embed(audio, sr)

    append_item(os.path.join(OUTPUT_DIR, "yamnet_apple_embeddings_v2.npy"), str(song_id), embedding)
    append_item(os.path.join(OUTPUT_DIR, "apple_song_names.npy"), str(song_id), song_name)
    print(f"Saved embedding singular for {song_name} to {OUTPUT_DIR}")

def main():
    apple_embedding_extraction()

if __name__ == "__main__":
    main()
