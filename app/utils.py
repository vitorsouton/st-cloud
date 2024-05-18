import librosa
import numpy as np


def get_spect():
    signal = librosa.load(
        'raw_data/0_01_0.wav'
    )[0]

    stft = librosa.stft(signal)[:-1]
    spectrogram = np.abs(stft)
    log_spectrogram = librosa.amplitude_to_db(spectrogram)

    norm = (log_spectrogram - log_spectrogram.min()) / (log_spectrogram.max() - log_spectrogram.min())

    return norm
