
'''
https://pythonprogramminglanguage.com/text-to-speech/

sudo apt install mpg321
sudo pip install gTTS
'''

from gtts import gTTS
import os

tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

