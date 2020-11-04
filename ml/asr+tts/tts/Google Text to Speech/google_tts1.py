
'''
https://pythonprogramminglanguage.com/text-to-speech/

sudo apt install mpg321
sudo pip install gTTS
'''

from gtts import gTTS
import os

tts = gTTS(text='Good morning', lang='en')

outfile = "/tmp/output.mp3"
tts.save(outfile)

# play sound and remove it	
os.system("mpg321 {}".format(outfile))
os.system("rm {}".format(outfile))

