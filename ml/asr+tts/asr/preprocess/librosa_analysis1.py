'''
librosa 를 이용한 Audio 전처리 - https://ahnjg.tistory.com/83

    1. Display Waveform
    2. FFT->Power spectrum
    3. SFTF->Spectrogram
    4. Cast Amplitude to Decibels
    5. MFCCs
'''

import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

#FIG_SIZE = (15,10)
FIG_SIZE = (10,5)
file = "okay-well.wav"


# 1. Display Waveform
def display_waveform(signal, sample_rate):
    plt.figure(figsize=FIG_SIZE)
    librosa.display.waveplot(signal, sample_rate, alpha=0.4)
    plt.xlabel("Time (s)")
    plt.ylabel("Aplitude")
    plt.title("Waveform")
    plt.show()

# 2. FFT->Power spectrum
def display_power_spectrum(signal, sample_rate):
    # Perform FFT
    fft = np.fft.fft(signal)
    print("fft shape: ", fft.shape)

    # Calculate abs values on complex numbers to get magnitude
    spectrum = np.abs(fft)
    print("spectrum shape: ", spectrum.shape)

    # Create Frequency Variable
    f = np.linspace(0, sample_rate, len(spectrum))
    print("f shape: ", f.shape)

    # take half of the spectrum and frequency
    left_spectrum = spectrum[:int(len(spectrum)/2)]
    left_f = f[:int(len(spectrum)/2)]
    print("left_spectrum shape: ", left_spectrum.shape)
    print("left_f shape: ", left_f.shape)

    # plot spectrum
    plt.figure(figsize=FIG_SIZE)
    plt.plot(left_f, left_spectrum, alpha=0.4)
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.title("Power spectrum")
    plt.show()

# 3. SFTF->Spectrogram
def display_spectrogram(signal, sample_rate):
    hop_length = 512    # in num. of samples
    n_fft = 2048        # window in num. of samples

    # calculate duration hop length and window in seconds
    hop_length_duration = float(hop_length)/sample_rate
    n_fft_duration = float(n_fft)/sample_rate

    print("STFT hop length duration is : {}s".format(hop_length_duration))
    print("STFT window duration is : {}s".format(n_fft_duration))

    # perform STFT
    stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)
    print("stft shape: ", stft.shape)

    # calcuate abs values on complex numbers to get magnitude
    spectrogram = np.abs(stft)
    print("spectrogram shape: ", spectrogram.shape)

    # display spectrogram
    plt.figure(figsize=FIG_SIZE)
    librosa.display.specshow(spectrogram, sr=sample_rate, hop_length=hop_length)
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.colorbar()
    plt.title("Spectrogram")
    plt.show()

    return spectrogram

def cast_amplitude_to_decibels(spectrogram, sample_rate):
    hop_length = 512    # in num. of samples
    
    # apply logarithm to cast amplitude to Decibels
    log_spectrogram = librosa.amplitude_to_db(spectrogram)
    print("log spectrogram shape: ", log_spectrogram)

    plt.figure(figsize=FIG_SIZE)
    librosa.display.specshow(log_spectrogram, sr=sample_rate, hop_length=hop_length)
    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram *dB")
    plt.show()

def get_MFCCs(signal, sample_rate):
    hop_length = 512    # in num. of samples
    n_fft = 2048        # window in num. of samples

    # Extract 13 MFCCs
    MFCCs = librosa.feature.mfcc(signal, sample_rate, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)
    print("MFCCs.shape: ", MFCCs.shape)

    # Display MFCCs
    plt.figure(figsize=FIG_SIZE)
    librosa.display.specshow(MFCCs, sr=sample_rate, hop_length=hop_length)
    plt.xlabel("Time")
    plt.ylabel("MFCC Coefficients")
    plt.colorbar()
    plt.title("MFCCs")
    plt.show()


def main():
    # load audio file with librosa
    signal, sample_rate = librosa.load(file, sr=44100)
    print("signal shape: ", signal.shape)

    # 1. Waveform
    display_waveform(signal, sample_rate)

    # 2. FFT --> Power spectrum
    display_power_spectrum(signal, sample_rate)

    # 3. SFTF --> Spectrogram
    spectrogram = display_spectrogram(signal, sample_rate)

    # 4. Cast Amplitude to Decibels
    cast_amplitude_to_decibels(spectrogram, sample_rate)
    
    # 5. MFCCs
    get_MFCCs(signal, sample_rate)

if __name__ == "__main__":
    main()
