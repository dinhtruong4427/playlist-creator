import numpy as np
from tqdm import tqdm

from neural_net.src.data_processes.audio_loader import load_apple_audio

def pad_audio(audio, target_len):
    if len(audio) > target_len:
        return audio[:target_len]
    elif len(audio) < target_len:
        return np.pad(audio, (0, target_len - len(audio)))
    return audio

def build_apple_batches(song_objects, batch_size=16, target_len=480000):
    batch = []
    names = []

    for song_object in tqdm(song_objects, desc="Preparing Ding's audio batches"):
        try:
            audio, sr = load_apple_audio(song_object[0])
            audio = pad_audio(audio, target_len)

            batch.append(audio)
            names.append(song_object[1])

            if len(batch) == batch_size:
                yield np.stack(batch), names
                batch = []
                names = []

        except Exception as e:
            print(f"Error batching {song_object[1]}: {e}")
    if batch:
        yield np.stack(batch), names