import pyttsx3
import os

#text that want  to convert to audio
txt_speech = pyttsx3.init()

speech = input("What text you want to convert to speech:")

#language you want to convert

language = "en"

txt_speech.say(speech)
txt_speech.runAndWait()

