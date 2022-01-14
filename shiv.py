import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import shutil
import random
import requests
import json
import time
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

def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")

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
   clear = lambda: os.system('cls')
   
   clear()
   wishMe()
   username()
   
   while True:
      query = takeCommand().lower()  

      if 'wikipedia' in query:
         speak ('searching wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak ("According to wikipedia")
         speak (results)
      
      elif 'how are you ' in query:
         speak ("I am good , How are you?")
      elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
   
      elif 'open youtube' in query:
         webbrowser.open("https://youtube.com")   
      elif 'open google' in query:
         webbrowser.open("https://google.com")     
      
      elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

      elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the Time is {strTime}")

      elif 'play music' in query or "play song" in query:
            speak("Here you go with music")   
            music_dir = "C:\\Users\KIIT\Downloads\songs"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
      
      elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

      elif "weather" in query:
            api_key = "d9825cf355fe5a71473bb238cdede267"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "&q=" + city_name + "&appid=" + api_key 
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                result = (" Temperature (in kelvin) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                speak(result)
                print(result)
             
            else:
                speak(" City Not Found ")    



      elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)


      elif 'open code' in query:
         codePath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
         os.startfile(codePath)      
      elif 'stop' in query:
       exit()
       
      



