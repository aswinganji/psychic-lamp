from tkinter import *
import speech_recognition as sr
import pyttsx3 
from datetime import datetime


text_to_speech = pyttsx3.init()
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    

root = Tk()
root.geometry("500x500")
def r_audio():
    speak("Bkah Blah Theif Catch Him! Pointy, You will not escape from me this time!")
    speech_recognisor= sr.Recognizer()
    with sr.Microphone() as source:
        print(voice_data)
        audio=  speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please repeat i did not get that')
            speak("What! YOU SAW Blah Blah Man?!")
    respond(voice_data)
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("Your name is WalkieTalkie")
    if "time" in voice_data:
        speak("10 days ago,The time  was What? I know that you don't know the answer. The Answer is What? 10 9 8 7 6 5 4 3 2 1 0 Time's up! The time 10 days ago is ")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
    
r_audio()
root.mainloop()