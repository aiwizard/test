'''
녹음, portaudio의 파이썬 버전
	https://kcal2845.tistory.com/35
	http://people.csail.mit.edu/hubert/pyaudio/
	
pip3 install pyaudio
'''

import pyaudio
import numpy as np
 
CHUNK = 2**8
RATE = 44100
 
p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK,input_device_index=2)
 
while(True):
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    print(int(np.average(np.abs(data))))
 
stream.stop_stream()
stream.close()
p.terminate()

