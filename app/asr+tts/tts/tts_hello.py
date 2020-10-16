from gtts import gTTS

txt = "Hello, Welcome to the Python world!"
tts = gTTS(text=txt, lang='en')
tts.save("hello.mp3")


ttskr = gTTS(text="안녕하세요", lang="ko")
ttskr.save("hello_in_korea.mp3")

