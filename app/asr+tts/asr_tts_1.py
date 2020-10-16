'''
https://davey.tistory.com/336


requirements
    pip install speechrecognition
    pip install gtts
    pip install playsound


1) Recognizer()
2) Microphone()
3) listen()
4) recognize_google()
'''


import speech_recognition as sr
from gtts import gTTS
import playsound

import os
import time

def reply(text, a):
    tts = gTTS(text=text, lang='en')
    filename = './text' + str(a) + '.mp3'

    # if os.path.isfile(filename):
    #    os.remove(file)

    tts.save(filename)
    playsound.playsound(filename)

def void_recognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    
    return said

i = 0
list01 = []

while True:
    text = void_recognition()

    if 'hi' in text:    # 1 번째 인식에 따른, 로봇의 답변 입력
        answer01 = 'hi long time no see how are you'
        reply(answer01, i)
        i = i+1
    elif 'how are you, can you tell me your name' in text:  #2 번째 인식에 따른, 로봇의 답변 입력
        answer01 = 'My name is Davey'
        reply(answer01, i)
    elif 'bye' in text:
        break

    list01.append(answer01 + str(i-1) + '.mp3')

for item in list01:
    print(item)
    os.remove('./' + item)
