'''
https://hyongdoc.tistory.com/401
'''

import librosa
import numpy as np
import matplotlib.pyplot as plt

audio_path = 'tonegen/6500Hz_5.0s.wav'
y, sr = librosa.load(audio_path)

stft_result = librosa.stft(y, n_fft=4096, win_length = 4096, hop_length=1024)
D = np.abs(stft_result)
S_dB = librosa.power_to_db(D, ref=np.max)
print('D.shape: {}\nS_dB.shape: {}'.format(D.shape, S_dB.shape))

#librosa.display.specshow(S_dB, sr=sr, hop_length = 1024, y_axis='linear', x_axis='time', cmap = cm.jet)
#plt.colorbar(format='%2.0f dB')
#plt.show()
