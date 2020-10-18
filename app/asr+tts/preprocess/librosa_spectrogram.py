'''
[Python 음성데이터 분석] Librosa로 Mel Spectrogram 생성

출처: https://hyongdoc.tistory.com/402 [Doony Garage]
'''

import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

n_fft = 2048
win_length = 2048
hop_length = 1024
n_mels = 128

print("Loading data ...")
y, sr = librosa.load(librosa.util.example_audio_file())
D = librosa.stft(y)
print(D)

D = np.abs(librosa.stft(y, n_fft=n_fft, win_length = win_length, hop_length=hop_length))
mel_spec = librosa.feature.melspectrogram(S=D, sr=sr, n_mels=n_mels, hop_length=hop_length, win_length=win_length)
librosa.display.specshow(librosa.amplitude_to_db(mel_spec, ref=0.00002), sr=sr, hop_length = hop_length, y_axis='mel', x_axis='time')#, cmap = cm.jet)
plt.colorbar(format='%2.0f dB')
plt.show()

freqs = librosa.cqt_frequencies(108, librosa.note_to_hz('C1'))
aw = librosa.A_weighting(freqs)
plt.plot(freqs, aw)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Weighting (log10)')
plt.title('A-Weighting of CQT frequencies')
plt.show()
