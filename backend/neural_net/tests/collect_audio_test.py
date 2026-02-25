from src.data_processes.audio_indexing import collect_audio_files, collect_apple_samples
from src.config.embedding_config import AUDIO_ROOT, APPLE_ROOT

audio_files = collect_audio_files(AUDIO_ROOT)
apple_urls = collect_apple_samples(APPLE_ROOT)

print(audio_files[:5])
print(apple_urls[:5])
