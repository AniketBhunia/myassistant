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
      elif 'image of a cat' in query:
         webbrowser.open("https://www.google.com/search?q=cat+images&sxsrf=AOaemvKACa5AwGHOmotUfp8E9ZL21uA-DA:1640709754272&tbm=isch&source=iu&ictx=1&fir=--16yG3LYPKNHM%252CrNJwENmHQ-ZHoM%252C_%253B_tJ9zISYcJ92GM%252CrzUo6RAz-vdsGM%252C_%253Baiul5-jr8DbWEM%252C6MsMJjk6eGCktM%252C_%253Br8gSbpVXU-d6FM%252CZx4TpH0a6gviqM%252C_%253BEs67tGnJFqXXFM%252CS6cybHMOSoZBQM%252C_%253BA_TJ5B4BpiRzNM%252CMia68JDKgpGbjM%252C_%253BNleIXKNfiJGUxM%252CFpFnzuctxfxSjM%252C_%253BSrn-aE4ZIIfbTM%252ChVpvvL-HxQGRYM%252C_%253BDfSaG3zDhKFujM%252ChVpvvL-HxQGRYM%252C_%253B037MLB2Kb6ZsfM%252C0xXBTE87P7Nj0M%252C_%253B6Igr2TbrhulyUM%252CK6Qd9XWnQFQCoM%252C_%253B9wap5LETXIiyeM%252CvmACvpHeD8wjzM%252C_%253B5uW4kYivZsexHM%252CCnZWxvwFxgFntM%252C_%253Bi5kllKf0o4WrfM%252CNtRtX0ni-SnqQM%252C_%253BesS6oQWQ5zwjyM%252Cx9jvP824aWKNPM%252C_%253BosXeu6XWatqycM%252CTmUkLtkPkKEi5M%252C_%253Bm4e4TjlJ1-TMZM%252CmIXEnR7F0v-RIM%252C_&vet=1&usg=AI4_-kQli5qCTlvEbMBVEH3XJP-YKwukDA&sa=X&ved=2ahUKEwjyiNSQ-Ib1AhX3sVYBHbYKC9UQ9QF6BAgDEAE#imgrc=--16yG3LYPKNHM")   

      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the Time is {strTime}")
      elif 'open code' in query:
         codePath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
         os.startfile(codePath)      
      if 'quit' in query:
       exit
       
      



