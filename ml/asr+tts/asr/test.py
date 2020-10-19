import speech_recognition as sr
import pyaudio

print('sr version: {}'.format(sr.__version__))
r = sr.Recognizer()	#initialization

with sr.Microphone() as source:
	print('Please say a command: ')
	audio = r.listen(source)
	
	try:
		text = r.recognize_google(audio, language='ko-KR')
		print('You said: {}'.format(text))
	except Exception as e:
		print('Error: {}'.format(e))

