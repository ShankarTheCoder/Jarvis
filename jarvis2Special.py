# import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib


import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')






# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')

# Check if voices are available
if voices:
    engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Ironman, Commander. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjusts to ambient noise
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivshankarpandit212@gmail.com', 'Shankar@20909')  # Use environment variables for security
    server.sendmail('shivshankarpandit212@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'gate khol' in query:
            speak("Chal,  chutiya")


        elif 'rajkumar' in query:
            speak("Gandu Bhosdi wala")

        elif 'lokesh' in query:
            speak("gandu bhosdibala")          

        elif 'prince' in query:
            speak("Bokachoda Sale")          

        elif 'stop program' in query:
             os.system("taskkill /im jarvis2Special.exe") 
                  



     


        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            # music_dir = 'C:\Users\dell\Music'
            music_dir = 'C:/Users/dell/Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[3]))


        elif 'stop music' in query.lower():
             # Code to stop the music
            os.system("taskkill /im VLC.exe")  # Replace with your music player command

# C:\Program Files\VideoLAN\VLC\


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to pankaj' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pankajray1288@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")
        else:
            print("No query matched")





            