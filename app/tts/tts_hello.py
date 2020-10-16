from gtts import gTTS

txt = "Hello, Welcome to the Python world!"
tts = gTTS(text=txt, lang='en')
tts.save("hello.mp3")
