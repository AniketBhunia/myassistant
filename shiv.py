import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
engine  = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
       speak("Good morning!")


    elif hour>=12 and hour<16:
       speak("Good Afternoon!")

    else:
       speak("Good Evening!")

    speak("hey boss how can i help u ")
def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining.....")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
       print("Recognizing....")
       query = r.recognize_google(audio, language='en-in')
       print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
       print("say that again please.....")
       return "None"
    return query   
if __name__ == "__main__":
   wishMe()
   if 1:
      query = takeCommand().lower()  

      if 'wikipedia' in query:
         speak ('searching wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak ("According to wikipedia")
         speak (results)

      elif 'open youtube' in query:
         webbrowser.open("youtube.com")   
      elif 'open google' in query:
         webbrowser.open("google.com")     
      elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")   

      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the Time is {strTime}")
      elif 'open code' in query:
         codePath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
         os.startfile(codePath)      
      if 'quit' in query:
       exit
       
      



