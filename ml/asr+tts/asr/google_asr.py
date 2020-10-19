'''
https://pythonprogramminglanguage.com/speech-recognition/

Installation
	pip install python-pyaudio
	pip install SpeechRecognition

Demo
	We can test the speech recognition module, with the command:
		python -m speech_recognition
'''

import speech_recognition as sr  

while(True):
	# get audio from the microphone                                                                      
	r = sr.Recognizer()                                                                                  
	with sr.Microphone() as source:                                                                      
		print("Speak:")                                                                                   
		audio = r.listen(source)   

	try:
		#print("You said " + r.recognize_google(audio))

		recog_text = r.recognize_google(audio)	#default API KEY
		#recog_text = r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")
		print("You said: '{}'\n".format(recog_text))
		if(recog_text == "done testing"):
			break

	except sr.UnknownValueError:
		print("Could not understand audio")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))


print('bye')

