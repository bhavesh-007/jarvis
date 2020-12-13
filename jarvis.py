from tkinter import *
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import tkinter
import pywhatkit
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning User!")
        speak(" i am jarvis developed by mister programmer")
        speak("you are ready to speak!  speak now please")
        speak("hi")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon User!")
        speak(" i am jarvis developed by mister programmer")
        speak("you are ready to speak!  speak now please")
    else:
        speak("Good Evening User!")
        speak(" i am jarvis developed by mister programmer")
        speak("you are ready to speak!  speak now please")


def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening........")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("recognizing........")
            query = r.recognize_google(audio_data=audio, language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print("Say that again please.....")
            return "None"
        return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecmd().lower()
        #logics started here :
        if 'wikipedia' in query:
            speak('searching in wikipedia.....')
            query = query.replace('wikipedia', "")
            Result = wikipedia.summary(query, sentences=2)
            print(Result)
            speak("according to my data base")
            speak(Result)
            speak("ready to hear new command sir")

        if 'tell me about yourself' in query:
            speak(
                "i am jarvis developed by mister bhavesh mahawar,and i am capable of performing task and learn some new commands"
            )
            speak("ready to hear new command sir")

        if 'exit' in query:
            speak("bye have a nice day")
            exit(0)

        if 'time' in query:
            print(datetime.datetime.now().strftime('%I:%M:%S %p'))
            speak('current time is ' +
                  datetime.datetime.now().strftime('%I:%M:%S %p'))
            speak("ready to hear new command sir")

        if 'youtube' in query:
            song = query.replace('youtube', "")
            speak('Playing.. ' + song + 'on youtube')
            pywhatkit.playonyt(song)

        if 'message in whatsapp' in query:
            msg = query
            speak("tell me the number to send")
            takecmd()
            print(query)
        else:
            speak("ready to hear new command sir")
