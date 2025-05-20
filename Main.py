import speech_recognition as sr
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
    pass




