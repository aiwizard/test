'''
https://m.blog.naver.com/PostView.nhn?blogId=bdh0727&logNo=221266874029
'''

import librosa
from scipy import signal
from scipy.io import wavfile


sound_path = "test.wav"

# using scipy only
#scipy_sr, scipy_wav = wavfile.read(sound_path)
#freq_axis, t_axis, spec = signal.spectrogram(x=scipy_wav, fs=48000, nperseg=400, noverlap=240, nfft=512)


# using librosa and scipy
samples, sample_rate = librosa.load(path=sound_path, sr=48000, mono=True, duration=1)
# mono = True   : True=1, False=2
# duration = 1  : 1 sec

freq_axis, t_axis, spec = signal.spectrogram(x=samples, fs=48000, nperseg=400, noverlap=240, nfft=512)
# x         : input signal
# fs        : sampling frequency
# nperseg   : window size (0.01s 를 window size 로 하기 위해 48000 * 0.01 = 480)
# noverlap  : number of overlap segments (overlap ratio = 0.5 이기 때문에 480 * 0.5 = 240)
# nfft      : FFT의 windows size 라는데 FFT를 적용할 size 를 뜻하는 듯. window size 보다 큰 2의 지수승을 보통 사용한다

# spec 에 스펙트로그램이 저장되어 있다. shape: (257, 199)
