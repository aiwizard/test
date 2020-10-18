'''
Librosa python library로 음성파일 분석하기

출처: https://banana-media-lab.tistory.com/7 [Banana Media Lab]

'''

import librosa
import librosa.display
#import IPython.display
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

#%matplotlib inline

# 1. 음성 파일 load
#audio_path = 'data/1_0000_trim.wav'
audio_path = 'okay-well.wav'
y, sr = librosa.load(audio_path)
ori_sent = '그는 괜찮은 척 하려고 애쓰는 것 같았다'

# 2. 음성 파일 load 확인
# IPython.display.Audio(data=y, rate=sr)

D = librosa.amplitude_to_db(librosa.stft(y[:1024]), ref=np.max)
 
plt.plot(D.flatten())
plt.show()

# 3. MFCC
#   음성 데이터를 더 잘 분석하기 위해, MFCC를 수행한 후, amplitude를 log scale로 변환하도록 하겠다.
S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128) 

#log_S = librosa.logamplitude(S, ref_power=np.max)  # deprecated
log_S = librosa.power_to_db(S, ref=np.max)
plt.figure(figsize=(12, 4))
librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
plt.title('mel power spectrogram')
plt.colorbar(format='%+02.0f dB')
plt.tight_layout()
plt.show()

# 4. Normalization
#   값의 범위가 -80-0이면 다루기가 쉽지 않으니, normalization을 수행할 것이다.
min_level_db = -100
 
def _normalize(S):
    return np.clip((S - min_level_db) / -min_level_db, 0, 1)


norm_S = _normalize(log_S)
 
plt.figure(figsize=(12, 4))
librosa.display.specshow(norm_S, sr=sr, x_axis='time', y_axis='mel')
plt.title('norm mel power spectrogram')
plt.colorbar(format='%+0.1f dB')
plt.tight_layout()
plt.show()

# 이제 음성 데이터를 '이미지'처럼 다룰 수 있도록 0-1로의 값으로 표현할 수 있게 되었다.


# 5. 음성 데이터 자르기
#   난 자소 단위로 음성 데이터를 자르기를 원하니, 먼저 입력 문장을 자소 단위로 쪼게보도록 하겠다.
#   라이브러리는 hgtk를 사용했는데, 가장 간편하고 빠른 것 같다.
import hgtk
 
jamo_sent = hgtk.text.decompose(ori_sent)
jamo_sent = jamo_sent.replace('ᴥ', '')
print(jamo_sent)

time_frame_num = 140

# 이제 자소 개수만큼 음성 데이터를 잘라보자.
char_frame_num = int(time_frame_num / len(jamo_sent)) #가로 사이즈
print(char_frame_num)
print(time_frame_num)

mpl.rc('font', family="NanumBarunGothic")
plt.figure(figsize=(20, 150))
jamo_sent_size = len(jamo_sent)
for i in range(0, jamo_sent_size):
    plt.subplot(jamo_sent_size, 5, i+1)
    start_position = (i * char_frame_num) - 1
    end_position = ((i+1) * char_frame_num) + 1
    if(start_position < 0):
        start_position = 0
        end_position = end_position + 1
    if(end_position > time_frame_num):
        start_position = start_position - (end_position - time_frame_num)
        end_position = time_frame_num
    window = norm_S[0:mel_freq_num, start_position:end_position]
    plt.pcolor(window, cmap='jet')
    plt.title(str(jamo_sent[i]))
    plt.colorbar()
    plt.show()
    