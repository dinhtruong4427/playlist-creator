import torch
import numpy as np
from panns_inference import AudioTagging
from panns_inference.models import Cnn14

class PANNsEmbedder:
    def __init__(self, device='cuda'):

        if torch.cuda.is_available() and device == 'cuda':
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')
        self.model = Cnn14(sample_rate=32000,
                           window_size=1024,
                           hop_size=320,
                           mel_bins=64,
                           fmin=50,
                           fmax=14000,
                           classes_num=527)

        self.checkpoint = torch.hub.load_state_dict_from_url(
            "https://zenodo.org/record/3987831/files/Cnn14_mAP=0.431.pth",
            map_location=device
        )
        self.model.load_state_dict(self.checkpoint['model'])
        self.model.to(self.device)
        self.model.eval()


    def embed(self, audio, sr=32000, sample_len=30):
        '''
        Extract embeddings from audio using PANNs Cnn14 model.
        Args:
            audio (np.ndarray): Input audio waveform.
            sr (int): Sample rate of the input audio.
            sample_len (int): Length of audio samples in seconds.
        '''
        audio_tensor = torch.tensor(audio, dtype=torch.float32).unsqueeze(0).to(self.device)
        with torch.no_grad():
            embedding = self.model(audio_tensor)

        return embedding['embedding'].squeeze(0).cpu().numpy()

