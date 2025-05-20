The Name Must be Patrick.
First of all in order to make something personal, We need 3 key items to consider.
1. Strong Firewall security
2.Image Recognition for Face Recognition
3. Exclude vulgar words but if someone wants to it'll be as a choice.
To fully execute personalized AI assistance, it's essential to give it some human like feature. like greetings,Empathy,Tonal changes. 
Here's the Entrée,

" import speech_recognition as sr
import pyttsx3
import pyaudio

listener = sr.Recognizer()

try:
    with sr.Microphone()as source:
        print('Concentrating....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)

except:
    pass " 
