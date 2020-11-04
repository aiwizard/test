
import os
from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
tts = gTTS('hello', lang='en')
tts.write_to_fp(mp3_fp)

# Load `mp3_fp` as an mp3 file in the audio library of your choice


