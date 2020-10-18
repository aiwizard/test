'''
https://blog.naver.com/gudrb1707/221283491146
'''

## 1. Import modules
import warnings
import matplotlib.pyplot as plt
import numpy as np
from numpy import arange, ones, pi
from scipy import cos, sin
from scipy.fftpack import fft, fftfreq, ifft
warnings.filterwarnings("ignore")    # 사소한 경고 무시


## 2. Set up for domain & Creating signal
n   = 100          # 한 파장당 지점 개수
Lx  = 10           # 한 파장의 거리 (혹은 시간)
L   = Lx/(2*pi)    # 파장
omg = 2.0*pi/Lx    # 각진동수
x   = arange(0, n)/Lx       # x축 : n개의 지점, Lx의 길이를 한 파장으로 가정
y1  = 5.0*sin( 2.0*omg*x)   # 파수  2에 해당하는 사인파
y2  = 4.0*cos( 3.0*omg*x)   # 파수  3에 해당하는 코사인파
y3  = 1.0*sin(10.0*omg*x)   # 파수 10에 해당하는 사인파
y   = y1 + y2 + y3 # + 1    # 임의의 파동 y (상수값을 추가하려면 주석을 해제할 것)


## 3. Cross checks for power spectrum
mean_y = np.mean(y)    # 평균
std_y = np.std(y)      # 표준편차
var_y = std_y**2.0     # 분산

print("Signal mean : %.2f, standard variation : %.2f, variance : %.2f" 
       % (mean_y, std_y, var_y))


## 4. Preparatory steps
freqs = fftfreq(n)        # 필요한 모든 진동수를 만든다.
mask = freqs > 0          # 절반의 값을 무시
nwaves = freqs*n          # 도메인 길이에 따른 파수
times = 1.0/freqs         # 시간 주기
times[freqs == 0.0] = Lx  # 각진동수가 0일때 Lx의 값을 할당


## 5. Power Spectrum calculation
fft_vals = fft(y)                               # FFT 계산
fft_norm = fft_vals*(1.0/n)                     # FFT 계산된 결과를 정규화
ps = 2.0*(np.abs(fft_norm)**2.0)                # 파워 스펙트럼
psa = 2.0*np.sqrt(fft_norm*np.conj(fft_norm))   # 파워 스펙트럼 진폭
fft_theo = 2.0*abs(fft_norm)                    # 푸리에 계수 계산
pow_var = ps/var_y*100   # 파워 스펙트럼 기여도(%)
fps = ps*freqs    # 각진동수 파워


## 6. Check result
print("Sum of Power Specturm : ", np.sum(ps[mask]))

# 1. 임의의 파동 y
plt.figure(1)
plt.title('Original Signal')
plt.plot(x, y, color='xkcd:salmon', label='original')
plt.legend()

# 2. 푸리에 계수
plt.figure(2)
plt.bar(nwaves[mask], fft_theo[mask], label="true fft values")
plt.title("True FFT values")
plt.legend()

# 3. 파워 스펙트럼
plt.figure(3)
plt.bar(times[mask], ps[mask], label="timeperiod vs spectra")
plt.title("Power Spectrum Example - timeperiod vs spectra")
plt.legend()

# 4. 파워 스펙트럼 기여도
plt.figure(4)
plt.bar(nwaves[mask], pow_var[mask], label="wavenumber vs power by variance")
plt.title("Power Spectrum Example - wavenumber vs power by variance")
plt.legend()
plt.show()
