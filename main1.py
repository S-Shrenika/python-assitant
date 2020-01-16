import os
import time
import speech_recognition as sr
import pyttsx3
import datetime
import subprocess

def speak(text):
	engine= pyttsx3.init()
	engine.say(text)
	engine.runAndWait()
speak("hello i am your assistant")

def getaudio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""
		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("exception" + str(e))
	return said

def note(text):
	date=datetime.datetime.now()
	filen=str(date).replace(":","-") + "note.txt"
	with open(filen, "w") as f:
		f.write(text)
	subprocess.Popen(["notepad.exe", filen])

def process(input):
	try:
		if 'open' in input:
			open_application(input.lower())
		else:
			speak("i dont understand")
	except:
		speak("bye")
    
def open_application(input): 
    if "chrome" in input: 
        speak("Google Chrome") 
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
        return
    else:
        speak("Application not available") 
        return
	
wake="hey assistant"
print("start")
while True:
	print("listening")
	text=getaudio().lower()
	if text.count(wake)>0:
		speak("please tell me what you want me to do")
		text=getaudio().lower()
		note_st = ["make a note","write this down","remeber this"]
		for i in note_st:
			if i in text:
				speak("what do you want me to make a note of?")
				note_mak=getaudio().lower()
				note(note_mak)
				speak("done")
		process(text)
