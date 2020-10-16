
from playsound import playsound

try:
    playsound("/home/munhwan/바탕화면/work/test/app/asr+tts/tts/hello.mp3")
except Exception as e:
    print(e)


print('press any key to quit...')
print(input())

