import librosa
import numpy as np
import requests
import tempfile
import subprocess
import os


'''
function to take in mp3 files and turn into waveform
path: path to audio file
sr (sample rate): 44100 for standard CD quality
mono: audio type
duration: length of clip
'''
def load_audio(path, sr=44100, mono=True, duration=None):
    # reads audio file and converts into wave form
    y, orig_sr = librosa.load(path, sr=sr, mono=mono,duration=duration)
    # ensures wave form is in proper form 
    y = y.astype(np.float32)

    # scales wave form to ensure -1 < y < 1
    if np.max(np.abs(y)) > 0:
        y /= np.max(np.abs(y))

    return y, sr

def load_apple_audio(url, sr=44100, mono=True, duration=None):
    # Download preview
    retrieved_audio = requests.get(url, timeout=10)
    retrieved_audio.raise_for_status()

    with tempfile.NamedTemporaryFile(suffix=".m4a", delete=False) as f:
        f.write(retrieved_audio.content)
        input_path = f.name

    output_path = input_path.replace(".m4a", ".wav")

    try:
        # Convert using ffmpeg
        subprocess.run(["ffmpeg", "-y",
                "-loglevel", "error",
                "-i", input_path,
                "-ac", "1",
                "-ar", str(sr),
                output_path
            ],
            check=True
        )

        # Load into librosa
        y, sr = librosa.load(output_path, sr=sr, mono=True)
        return y, sr

    finally:
        os.remove(input_path)
        if os.path.exists(output_path):
            os.remove(output_path)