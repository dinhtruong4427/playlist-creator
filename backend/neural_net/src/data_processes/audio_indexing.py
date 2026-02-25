import os
import csv
from tqdm import tqdm
'''
collects audio data and returns an array of the files
root: filepath to data
extensions: valid audio file endings
'''
def collect_audio_files(root, extensions=(".mp3", ".wav")):
    # array for audio files
    audio_files = []

    # loops through folders and subfolders
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            # adds if name ends with audio valid file types
            if fname.lower().endswith(extensions):
                audio_files.append(
                    os.path.join(dirpath, fname)
                )
    return sorted(audio_files)

'''
collects csv links and returns an array of tuples (url, trackId, trackName)
root: filepath to apple data csv
'''
def collect_apple_samples(root):
    sample_list = []

    with open(root, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in tqdm(reader):
            try:
                song_object = (row["previewUrl"], row["trackId"], row["trackName"])
                sample_list.append(song_object)
            except Exception as e:
                print(f"Skipping {row['trackName']}: {e}")

    return sample_list