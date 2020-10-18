'''

출처: https://hhhhhhhong.tistory.com/39 [OukVeloper]
'''

# Beat tracking example
#from __future__ import print_function
import librosa


# 1. Get the file path to the included audio example
filename = "/home/munhwan/다운로드/wav/okay-well.wav"

#핵심은 완전하게 경로를 써줄것


# 2. Load the audio as a waveform `y`
# Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print('saving')
librosa.output.times_csv('./1beat_time.csv',beat_times)
