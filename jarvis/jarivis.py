import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.runAndWait()
import speech_recognition as sr #pip install speechRecognition
import datetime



def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


# def wishMe():
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
        speak(f"Good Morning sir !,{welcome.mp3} ")

elif hour>=12 and hour<18:
        speak("Good Afternoon sir!,{welcome.mp3}")   

else:
        speak("Good Evening sir!,{welcome.mp3}")  

#speak("I am Jarvis Sir. Please tell me how may I help you") 