# import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
# import smtplib
import pyaudio
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
    speak("I am Julie. Please tell me how may I help you")

def alarmClock():
     hr = int(datetime.datetime.now().hour)
     min = int(datetime.datetime.now().minute)
     if hr==5 and min==00:
         speak("Wake Up My Bhaiya, Uth Jao, Subah HoGya!!")
     elif hr==8 and min==00:
         speak("Go for having Breakfast, Bhaiya!!")
    

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

def sendEmail(subject, body, to_email):
    sender_email = "techyray35@gmail.com"
    password = "tyie dcru ifgc rrsc"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, to_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

if __name__ == "__main__":
    wishMe()
    alarmClock()
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

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'gate khol' in query:
            speak("Chal,  chutiya")


        elif 'rajkumar' in query:
            speak("RajKumar, Bhosdi wala")

        elif 'lokesh' in query:
            speak("Lokesh, Machikne")          

        elif 'prince' in query:
            speak("Chal beta aage Chal")          

        elif 'stop program' in query:
             os.system("taskkill /im jarvis2Special.exe") 

      

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'play music' in query:
            # music_dir = 'C:\Users\dell\Music'
            music_dir = 'C:/Users/Lokesh Bohara/Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))


        elif 'stop music' in query.lower():
             # Code to stop the music
            os.system("taskkill /im VLC.exe")  



        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Bhaiya, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C://Users//Lokesh Bohara//AppData//Local/Programs//Microsoft VS Code//Code.exe"
            speak("is opening")
            os.startfile(codePath)

        elif 'open brave' in query:
            codePath = "C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe"
            os.startfile(codePath)

        elif 'open ms edge' in query:
            codePath = "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"
            os.startfile(codePath)

        elif 'email' in query:
           speak("What's the subject?")
           subject = takeCommand()
           
           speak("What to say?")
           body = takeCommand()
           
           to_email = "pankajray1288@gmail.com"
           sendEmail(subject, body, to_email)
           

        else:
            print("No query matched")





            