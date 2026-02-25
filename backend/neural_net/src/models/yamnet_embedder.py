import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

class YAMNetEmbedder:
    def __init__(self):
        # loads yamnet model from tensorflow hub
        self.model = hub.load("https://tfhub.dev/google/yamnet/1")
    '''
    creates an embedding for a single audio
    audio: waveform of audio (float32)
    sr (sample rate): yamnet requires 16 kHz
    '''
    def embed(self, audio, sr): 
        if sr != 16000:
            # ensures 16000 kHz audio is used
            audio = tf.signal.resample(audio, int(len(audio) * 16000 / sr))
        #converts waveform to tensorflow tensor
        audio = tf.convert_to_tensor(audio, dtype=tf.float32)

        scors, embeddings, spectogram = self.model(audio)

        return np.mean(embeddings.numpy(), axis=0)
    
    def embed_batch(self, audio_batch):
        """
        audio_batch: np.ndarray of shape (B, T)
        returns: np.ndarray of shape (B, 1024)
        """
        batch_embeddings = []

        for audio in audio_batch:
            audio = tf.convert_to_tensor(audio, dtype=tf.float32)

            scores, embeddings, spectrogram = self.model(audio)

            # Mean-pool frame embeddings
            song_embedding = tf.reduce_mean(embeddings, axis=0)
            batch_embeddings.append(song_embedding.numpy())

        return np.stack(batch_embeddings)