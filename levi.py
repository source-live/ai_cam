import pyaudio
import speech_recognition as sr
import pyttsx as tts
import webbrowser
import sys
from difflib import SequenceMatcher

# --  Define System Variables
r = sr.Recognizer()
source = sr.Microphone

# --  File to read if command Read said.
file = sys.args[0]

# --  Define say() Function
def say(levi2=""):
  tts.init().say(levi2)
  
# --  Define similar() Function
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# --  Wait for input

with sr.Microphone as source:
  input = r.listen(source)
  
  # --  Define commands :)
  if similar("Hello",r.recognize_sphinx(audio)) > 0.4: # Hello.
    say("Hello.")
    print(similar("Hello",r.recognize_sphinx(audio)))
  elif similar("What's up",r.recognize_sphinx(audio)) > 0.4: # What's up?
    say("Nothing.  What about you?")
    print(similar("What's up",r.recognize_sphinx(audio)))
  elif similar("Do you like me",r.recognize_sphinx(audio)) > 0.4: # Do you like me?
    say("Maybe.  Do I?") # Sauce
    print(similar("Do you like me",r.recognize_sphinx(audio)))
  elif similar("I hate you",r.recognize_sphinx(audio)) > 0.4: # I hate you.
    say("Why do you hate me?")
    print(r.recognize_sphinx(audio))
  elif similar("Good morning",r.recognize_sphinx(audio)) > 0.4: # Good morning.
    say("Good morning, master.")
    print(r.recognize_sphinx(audio))
  elif similar("Good night",r.recognize_sphinx(audio)) > 0.4: # Good night.
    say("Good night, master.")
    print(r.recognize_sphinx(audio))
  elif similar("Google",r.recognize_sphinx(audio)) > 0.4: # Google
    say("I am opening google.")
    webbrowser.open('https://google.com')
    print(r.recognize_sphinx(audio))
  elif similar("Bing",r.recognize_sphinx(audio)) > 0.4: # Bing
    say("I am opening bing.")
    webbrower.open('https://bing.com')
    print(r.recognize_sphinx(audio))
  elif similar("Git hub",r.recognize_sphinx(audio)) > 0.4: # Github
    say("I am opening github.")
    webbrower.open('https://github.com')
    print(r.recognize_sphinx(audio))
  elif similar("Where were you made",r.recognize_sphinx(audio)) > 0.4: # Where were you made
    say("I will open the link of where I was originally made.")
    webbrowser.open('https://github.com/source-live/levi2')
    print(r.recognize_sphinx(audio))
  elif similar("Will you marry me",r.recognize_sphinx(audio)) > 0.4: # Will you marry me?
    say("Sorry, but I am not even a year old as of this version.")
    print(r.recognize_sphinx(audio))
  elif similar("Can we be friends",r.recognize_sphinx(audio)) > 0.4: # Can we be friends?
    say("Sure.")
    print(r.recognize_sphinx(audio))
  elif similar("Who made you",r.recognize_sphinx(audio)) > 0.4: # Who made you?
    say("Zack, the owner of Source-Live.  Check him out here.")
    webbrowser.open('https://github.com/sayRequil')
    print(r.recognize_sphinx(audio))
  elif similar("Read",r.recognize_sphinx(audio)) > 0.4: # Read
    say("I will read the file you inputed.  I prefer .txt files.")
    # say(open(file,"r"))
    fl = len(f)
    fl2 = (fl-4)
    fla = file[fl2:fl]
    if fla == ".txt":
      say(open(file,"r"))
    
    print(r.recognize_sphinx(audio))
  elif similar("Bye",r.recognize_sphinx(audio)) > 0.4: # Bye
    say("Good bye, master.")
    print(r.recognize_sphinx(audio))
  elif similar("Shut up",r.recognize_sphinx(audio)) > 0.4: # Shut up
    say("Why are you being mean?")
    print(r.recognize_sphinx(audio))
