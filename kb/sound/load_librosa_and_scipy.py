'''
librosa.load 와 scipy.io.wavfile.read 의 차이

https://ahnjg.tistory.com/84
'''

from scipy.io import wavfile
import librosa
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

wav_file = 'okay-well.wav'

scipy_sr, scipy_wav = wavfile.read(wav_file)
librosa_wav, librosa_sr = librosa.load(wav_file, sr=None)

#Scipy
print("scipy_wav.shape: ", scipy_wav.shape)
print("scipy_wav[0].type: ", type(scipy_wav[0]))
print("scipy_sr: ", scipy_sr)
print()

#Librosa
print("librosa_wav.shape: ", librosa_wav.shape)
print("librosa_wav[0].type: ", type(librosa_wav[0]))
print("librosa_sr: ", librosa_sr)

sns.displot(scipy_wav)
sns.displot(librosa_wav)
plt.show()
