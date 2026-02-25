# package imports
import os
import numpy as np
from tqdm import tqdm

# file imports
from neural_net.src.data_processes.audio_indexing import collect_audio_files, collect_apple_samples
from neural_net.src.data_processes.audio_loader import load_audio, load_apple_audio
from neural_net.src.data_processes.batch_builder import build_apple_batches
from neural_net.src.models.panns_embedder import PANNsEmbedder
from neural_net.src.config.embedding_config import APPLE_ROOT, AUDIO_ROOT, OUTPUT_DIR, DURATION, SAMPLE_RATE

def local_embedding_extraction():
    # verifies if the output exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # collect audio files
    audio_files = collect_audio_files(AUDIO_ROOT)
    print(f"Found {len(audio_files)} audio files")

    # set embedding
    embedder = PANNsEmbedder()
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
    embedder = PANNsEmbedder(device='cpu')
    embeddings = []
    paths = []

    for song_obj in tqdm(audio_files, desc="Processing Ding's apple audio files"):
        try:
            # load audio file from path
            audio, sr = load_apple_audio(song_obj[0], sr=32000, duration=30)
            # converts audio into vectors and embeds into model
            emb = embedder.embed(audio)

            # adds embedding and path
            embeddings.append(emb)
            paths.append(song_obj[1])

        except Exception as e:
            print(f"Skipping {song_obj[1]}: {e}")

    # convert list of embeddings to a single matrix
    embeddings = np.stack(embeddings)

    # save outputs
    np.save(os.path.join(OUTPUT_DIR, "yamnet_apple_embeddings.npy"), embeddings)
    np.save(os.path.join(OUTPUT_DIR, "apple_urls.npy"), paths)

    print(f"Saved {len(embeddings)} embeddings to {OUTPUT_DIR}")

def main():
    apple_embedding_extraction()

if __name__ == "__main__":
    main()