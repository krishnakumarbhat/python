from urllib import request
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
from typing import Text
from googletrans import Translator
import os
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from pytube import YouTube
import datetime
import wikipedia
import pyautogui
import keyword
import keyboard
import pyjokes
import playsound 
from PyDictionary import PyDictionary as Diction
from bs4 import beautifulsoap 
from jarivis import speak
import pypdf2
import speedtest 
Assistent = pyttsx3.init('sapi5')
voices = Assistent.getProperty('voices')
# print(voices)
Assistent.setProperty('voices', voices[0].id)
Assistent.setProperty('rate', 180)


def Speak(audio):
    print("   ")
    Assistent.say(audio)
    print(f"  :{audio}")
    print("   ")
    Assistent.runAndWait()


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


def TaskExe():
    def music():
        Speak("Tell Me the nameof the song")
        musicName = takecommand()

        if 'back in back' in musicName:
            os.startfile('')
        elif 'what ever it takes' in musicName:
            os.startfile('')
        else:
            pywhatkit.playonyt(musicName)
        Speak("your song is here enjoy yourself, sir")

    def whatsapp():
        Speak("Tell Me The Name Of the Person")
        name = takecommand()

        if'amma' in name:
            Speak("tell me the message, sir")
            msg = takecommand()
        #   Speak('tell at what day')
        #   day = int(takecommand())
            Speak('tell at what hour sir')
            hour = int(takecommand())
            Speak('tell at what minute')
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919449751218", msg, hour, min, 20)
            Speak(f"sending whatsapp message to{name}")
        else:
            Speak("sir tell me the number")
            phone = int("please tell me the number sir")
            Speak("tell me the message, sir")
            msg = takecommand()
        #   Speak('tell at what day')
        #   day = int(takecommand())
            Speak('tell at what hour sir')
            hour = int(takecommand())
            Speak('tell at what minute')
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+919449751218", msg, hour, min, 20)
            Speak(f"sending whatsapp message to{name}")

    def OpenApps():
        Speak(f"ok sir, intialllizing {query}")

        if'python' in query:
            os.startfile(
                r"C:\Users\bhatk\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9")
        elif'power shell' in query:
            os.startfile(
                '%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe')
        elif'obs' in query:
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OBS Studio')
        elif'vscode' in query:
            os.startfile(
                r'C:\Users\bhatk\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code')
        elif'download manger' in query:
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Xtreme Download Manager')
        elif'kali linux' in query:
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle VM VirtualBox')
        elif'brave' in query:
            os.startfile(
                "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")

    def taskkill():
        Speak(f"ok sir , killing {query} task")

        if'python' in query:
            os.system("TASKKILL /f /in Python 3.9")
        elif'power shell' in query:
            os.system('TASKKILL /f /in powershell.exe')
        elif'obs' in query:
            os.system('TASKKILL /f /in OBS Studio')
        elif'vscode' in query:
            os.system("TASKKILL /f /in Visual Studio Code.exe")
        elif'download manger' in query:
            os.system("TASKKILL /f /in Xtreme Download Manager.exe")
        elif'kali linux' in query:
            os.system("TASKKILL /f /in brave.exe")

        Speak(f"sir i have killed the {query}task")

    def youtubeauto():
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('space bar')
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('l')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'initialize full screen' in comm:
            keyboard.press('t')

    def braveauto():
        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl+w')
        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl+t')
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl+n')
        elif 'show history' in command:
            keyboard.press_and_release('ctrl+h')

    def Dict():
        Speak('yes sir,tell the problem')
        prob1 = takecommand()

        if 'meaning' in prob1:
            prob1 = prob1.replace("what is the ", "")
            prob1 = prob1.replace("jarvis", "")
            probl = prob1.replace("meaning of")
            result = Diction.meaning(prob1)
            Speak(f'The meaning for {prob1} is {result}')
        elif'synonym' in prob1:
            prob1 = prob1.replace("what is the ", "")
            prob1 = prob1.replace("jarvis", "")
            probl = prob1.replace("synonym of")
            result = Diction.meaning(prob1)
            Speak(f'The synonym for {prob1} is {result}')
        elif'antonym' in prob1:
            prob1 = prob1.replace("what is the ", "")
            prob1 = prob1.replace("jarvis", "")
            probl = prob1.replace("antonym of")
            result = Diction.meaning(prob1)
            Speak(f'The antonym for {prob1} is {result}')

    def screenshot():
        Speak("ok sir,taking screen shot")
        Speak("sir, tell the name for this")
        path = takecommand()
        pathname = path + ".png"
        path1 = "D:\\com backup\\screenshot\\"+pathname
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile('D:\\com backup\\screenshot\\')
        speak("opening screenshot")

    def kannadatans():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening..")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognising..")
                query = command.recognize_google(audio, language='kan')
                print(f"You said  : {query}")

            except:
                print("sari kallila matondsala hale")
                return "none"

            return query.lower()

    def transl():
        Speak("tell me transalation line !")
        line = Takekannada()
        translate =  Translator()
        result =translate.translate(line)
        Text = result.text
        Speak(f"Tranlated line is :" + Text)

    def Temp():
        search = "temptature in honavar"
        url = "https://ww.google.com/search?=q="+search 
        r = request.get(url)
        data = beautifulsoap(r.text,"html.parser")
        temprature = data.find("div",class="bNeawe").text
        Speak(f"The temprature outside is {temprature} cesclius")
    
    def Speedtest():
        Speak("")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctupload = int(uploading/800000)
        Speak(f"sir speed of net is quit intutive that is {uploading}M B P S upload and {downloading}M B P S downloading speed") 

    while True:
        query = takecommand()

        if 'hello' in query:
            Speak("Hello sir,jarvis here ")
        elif'how are you' in query:
            Speak('I am fine ,what about you sir')
        elif' i need break' in query:
            Speak('sure sir  enjoy your break sir!')
        elif'bye jarvis' in query:
            Speak('Good bye sir')
        elif'youtube search' in query:
            Speak('sure sir')
            query = query.replace("jarvis", "")
            query = query.replace("make youtube search", "")
            web = 'https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
            Speak(f"sir, i have compiled {query} database in youtube ")
        elif'google search' in query:
            Speak('sure sir')
            query = query.replace("jarvis", "")
            query = query.replace("do google search", "")
            pywhatkit.search(query)
            Speak(f"sir, i have compiled {query} database in google ")
        elif'linkdin' in query:
            Speak('sure sir')
            query = query.replace("jarvis", "")
            query = query.replace("open my", "")
            web3 = 'https://www.linkedin.com/feed/'
            webbrowser.open(web3)
            Speak(f"sir, i have compiled {query} database in youtube ")
        elif'google schololer search' in query:
            Speak(f'sure sir ')
            query = query.replace("jarvis", "")
            query = query.replace("google scholar search", "")
            web = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+query
            webbrowser.open(web)
            Speak(f"sir, i have compiled {query} database in google scholer ")
        elif'website launch' in query:
            Speak(f'sure sir ')
            query = query.replace("jarvis", "")
            query = query.replace("website launch", "")
            web1 = query.replace("open", "")
            web2 = 'https://www.'+web1+'.com'
            webbrowser.open(web)
            Speak(f"sir, i have launched {query} continue your project")
        elif'music' in query:
            music()
        elif'wikipedia' in query:
            Speak("sure sir")
            query = query.replace("jarvis", "")
            query = query, os.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 15)
            Speak(f"According to this sir it says :{wiki}")
        elif'whatsapp message' in query:
            whatsapp()
        elif'screenshot' in query:
            screenshot()
        elif'open python' in query:
            OpenApps()
        elif'open vscode' in query:
            OpenApps()
        elif'open download manger' in query:
            OpenApps()
        elif'open power shell' in query:
            OpenApps()
        elif'open kali linux' in query:
            OpenApps()
        elif'open obs' in query:
            OpenApps()
        elif'open brave' in query:
            OpenApps()
        elif'close power shell' in query:
            taskkill()
        elif'close obs' in query:
            taskkill()
        elif'close python' in query:
            taskkill()
        elif'close brave' in query:
            taskkill()
        elif'close kali linux' in query:
            taskkill()
        elif'close vscode' in query:
            taskkill()
        elif'close download manager' in query:
            taskkill()
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'initialize full screen' in query:
            keyboard.press('t')
        elif'automate youtube' in query:
            youtubeauto()
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl+w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl+t')
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl+n')
        elif 'show history' in query:
            keyboard.press_and_release('ctrl+h')
        elif 'automate brave' in query:
            braveauto()
        elif 'dictionary' in query:
            Dict()
        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
        elif 'alarm' in query:
            Speak("please input your time sir")
            time = input("enter your time : ")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time to wake up , sir ")
                    Playsound("alarm.mp3")
                    Speak(
                        "I think sir, you deserve to work in and you have sleept more than 7 hours,good morning sir")
                elif now > time:
                    break
        elif 'video download ' in query:
            root = Tk()
            root.geometry('500X300')
            root.resizable(0, 0)
            root.title("youtube video downloader")

            Label(root, text="youtube video downloader",
                  font='ariel 15 bold').pack()
            link = StringVar()
            Label(root, text="paste the url here",
                  font='ariel 15 bold').place(x=160, y=60)
            Entry(root, width=70, textvariable=link).place(x=32, y=90)

            def videoDownloder():
                url = Youtube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root, text="Download", font='ariel 15').place(x=180, y=210)

            Button(root, text="Download", font='arial 15 hold',
                   bg='plae violet red', padx=2, command=videoDownloder)
            root.mainloop()
            Speak('sir,video has been downloaded')
        elif'translate'in query:
            transl()
        elif 'remember that' in query:
            rememberMsg = query.replace("remember that "," ")
            rememberMsg = rememberMsg.replace("jarvis","")
            speak("sir , you told me to remind you that :",rememberMsg)
            remember = open("datar.txt","W")
            remember.write(rememberMsg)
            remember.close()
        elif 'what do you remember' in query:
            remember = open('datar.txt','r')
            speak('sir,you told me that' + remember.read() ) 

        elif 'google search' in query:
            import wikipedia as googleScarp
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            Speak(f"finding  {query} in google database")

            try:
                pywhatkit.search(query)
                result = googleScarp.summary(query,3)    
                Speak(result)
            except:
                Speak("sir , no result from this datsa base") 
        elif 'temprature' in query:
            Temp()
        elif 'speed of internet' in query:
            speedtest()

        
        else:
            Speak(f'{query}')
