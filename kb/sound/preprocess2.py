'''
Librosa 라이브러리를 이용한 주파수 분석 - https://hyongdoc.tistory.com/401


'''

import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt



def main():
    print("Loading data ...")
    y, sr = librosa.load(librosa.util.example_audio_file())
    D = librosa.stft(y)
    print(D)

    # Use left-aligned frames, instead of centered frames
    D_left = librosa.stft(y, center=False)
    print(D_left)

    # Use a shorter hop length
    D_short = librosa.stft(y, hop_length=64)
    print(D_short)

    # Display a spectrogram
    log_spectrogram = librosa.amplitude_to_db(D, ref=np.max)
    librosa.display.specshow(log_spectrogram,
                             y_axis='log', x_axis='time')
    plt.title('Power spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
