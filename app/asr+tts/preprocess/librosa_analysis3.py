'''
librosa 패키지로 스펙트럼 그리기

https://hanseokhyeon.tistory.com/10
'''

import numpy as np
import librosa
import matplotlib.pyplot as plt


sample_rate = 8000
n_fft = 512

data = np.fromfile("ANC_X_8k/boeing_FF.raw", dtype=np.int16)
data = data.astype(np.float) / 32767
data = librosa.stft(data[sample_rate // 4:sample_rate // 4 * 2], n_fft=n_fft)
data = np.mean(librosa.amplitude_to_db(np.abs(data)), axis=1)

plt.title('boeing')

plt.xlabel("Frequency[Hz]")
plt.xticks(range(0, n_fft//2+1, 32), np.arange(0, 4001, 500))
plt.xlim(0, n_fft//2)

plt.ylabel("Amplitude[dB]")

plt.plot(data, label='data', alpha=0.7)

plt.grid()
plt.legend()

fig = plt.gcf()

plt.show()
fig.savefig('boeing.png')
