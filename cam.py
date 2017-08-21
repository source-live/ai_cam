import pyaudio
import speech_recognition as sr
import pyttsx as tts

r = sr.Recognizer()
with sr.Microphone() as source:
  print("Say command")
  audio = r.listen(source)
    
def say(levi2=""):
  tts.init().say(levi2)
