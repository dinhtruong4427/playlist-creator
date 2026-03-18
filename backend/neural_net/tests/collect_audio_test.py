from neural_net.src.data_processes.audio_indexing import collect_audio_files, collect_apple_samples
from neural_net.src.config.embedding_config import AUDIO_ROOT, APPLE_ROOT

audio_files = collect_audio_files(AUDIO_ROOT)
apple_urls = collect_apple_samples(APPLE_ROOT)

print("audio files", audio_files[:5])
print("apple urls", apple_urls[:5])
