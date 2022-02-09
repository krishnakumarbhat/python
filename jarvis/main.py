import pyttsx3
import datetime
# from playsound  import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',180)

# def Speak(audio):
#     print("  ")
#     engine.say(audio)
#     print(f": {audio}")
#     print("  ")
#     engine.runAndWait()

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!,sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!,sir")   

    else:
        speak("Good Evening!,sir")  

    speak("")
