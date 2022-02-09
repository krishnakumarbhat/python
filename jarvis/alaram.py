import pyttsx3
import datetime

# from playsound  import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180)



def Speak(audio):
    print("  ")
    engine.say(audio)
    print(f": {audio}")
    print("  ")
    engine.runAndWait()

Speak("wake up sir, good morning ")