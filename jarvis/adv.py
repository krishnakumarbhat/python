
import pyttsx3
import os
import speech_recognition as sr

# Assistent = pyttsx3.init('sapi5')
# voices = Assistent.getProperty('voices')
# # print(voices)
# Assistent.setProperty('voices', voices[0].id)
# Assistent.setProperty('rate', 180)

# def Speak(audio):
#     print("   ")
#     Assistent.say(audio)
#     print(f"  :{audio}")
#     print("   ")
#     Assistent.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognising..")
            query = command.recognize_google(audio, language='en-in')
            print(f"You said  : {query}")

        except :
            # print("say that again!")
            return "none"

        return query.lower()


while True:

    wake_up = takecommand()
    if 'wake up' in wake_up:
        os.startfile("D:\\all python projects\\jarvis\\jarvis.py")
    else:
        print("not")
    


