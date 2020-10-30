'''
pip3 install playsound
'''

from playsound import playsound

try:
    playsound("/home/munhwan/___mywork/test/app/asr+tts/tts/hello.mp3")
except Exception as e:
    print(e)


print('press any key to quit...')
print(input())

