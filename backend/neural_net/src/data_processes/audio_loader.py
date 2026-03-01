import librosa
import numpy as np
import requests
import io
import av

'''
function to take in mp3 files and turn into waveform
path: path to audio file or file-like object
sr (sample rate): 44100 for standard CD quality
mono: audio type
duration: length of clip
'''
def load_audio(path, sr=44100, mono=True, duration=None):
    # reads audio file/buffer and converts into wave form
    # librosa.load can take a file path OR a file-like object (BytesIO)
    y, orig_sr = librosa.load(path, sr=sr, mono=mono, duration=duration)
    
    # ensures wave form is in proper form 
    y = y.astype(np.float32)

    # scales wave form to ensure -1 < y < 1
    if np.max(np.abs(y)) > 0:
        y /= np.max(np.abs(y))

    return y, sr

def load_apple_audio(url, sr=44100, mono=True, duration=None):
    try:
        # 1. Download the file
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        container = io.BytesIO(response.content)

        # 2. Use PyAV to open the container (handles AAC/M4A natively)
        with av.open(container) as v:
            stream = v.streams.audio[0]
            # Resample and decode simultaneously
            resampler = av.AudioResampler(
                format='fltp',
                layout='mono' if mono else 'stereo',
                rate=sr,
            )
            
            frames = []
            total_samples = 0
            for frame in v.decode(stream):
                # Handle duration limit if specified
                if duration and (total_samples / sr) >= duration:
                    break
                
                resampled_frames = resampler.resample(frame)
                for resampled_frame in resampled_frames:
                    frames.append(resampled_frame.to_ndarray())
                    total_samples += resampled_frame.samples

            y = np.concatenate(frames, axis=1).reshape(-1)
            
            # 3. Apply your normalization logic
            y = y.astype(np.float32)
            if np.max(np.abs(y)) > 0:
                y /= np.max(np.abs(y))

            return y, sr

    except Exception as e:
        print(f"Error loading Apple audio with PyAV: {e}")
        return np.array([], dtype=np.float32), sr