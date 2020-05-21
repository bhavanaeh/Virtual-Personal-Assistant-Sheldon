import pyttsx3
import datetime 
from datetime import date
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import urllib.request
import requests
import smtplib
import getpass
import random
import time
import sys

hellos = ["Hello!","What's up?","How's it going?","Hi!","Hey!"]


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Morning. Hope you had your cup of coffee?! Lets get to work!')
    elif hour>=12 and hour <18:
        speak('Good afternoon Bhavana! Nice to know that you are not taking a nap!')
    else:
        speak('Welcome back Bhavana, how can I help you this evening?')
    
    speak('I am Sheldon and I am going to try and make your life a tad bit easier! Lets jump right in, shall we?')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        #engine.say("Okay,here we go!")
        print('Listening...')
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print('Just confirming,this is what you said...',query)
    except Exception as e:
        print(e)
        print('Say that again,please!')
        return "None"
    return query

def sendemail(to_id,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    emailid=input('Enter your EmailID:')
    password=getpass.getpass('Enter your password:')
    server.login(emailid,password)
    server.sendmail(emailid,to_id,content)
    server.close()

if __name__ == "__main__":
    
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia:')
            print(results)
            speak(results)

        elif 'youtube' in query:
            print("Searching '"+ query +"' on YouTube...",sep='')
            speak('Opening YouTube!')
            webbrowser.open('https://www.youtube.com/results?search_query='+query)
            
        elif 'attendance' in query:
            speak('Opening your academia for you!')
            webbrowser.open('https://academia.srmist.edu.in/#View:My_Attendance')

        elif 'reddit' in query:
            speak('Opening Reddit!')
            webbrowser.open('https://www.reddit.com/')

        elif 'twitter' in query:
            speak('Opening Twitter!')
            webbrowser.open('https://twitter.com/home')

        elif 'instagram' in query:
            speak('Opening Instagram!')
            webbrowser.open('https://www.instagram.com/?hl=en')

        elif 'github' in query:
            speak('Opening GitHub!')
            webbrowser.open('https://github.com/')

        elif 'apple music' in query:
            speak('Opening iTunes online!')
            webbrowser.open('https://music.apple.com/library/songs')

        elif 'linkedin' in query:
            speak('Opening LinkedIn')
            webbrowser.open('https://www.linkedin.com/feed/')

        elif 'stackoverflow' in query:
            speak('Opening StackOverflow!')
            webbrowser.open('https://stackoverflow.com/')

        elif 'classroom' in query:
            speak('Opening Google Classroom!')
            webbrowser.open('https://classroom.google.com/u/1/h')
        elif 'google' in query:
            speak('Opening Google!')
            webbrowser.open('https://www.google.com/')

        elif 'pinterest' in query:
            speak('Opening Pinterest!')
            webbrowser.open('https://in.pinterest.com/')

        elif 'time' in query or 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            speak('Opening Visual Studio Code!')
            codepath="C:\\Users\\bhava\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

            """
        elif 'google chrome' in query:
            speak('Opening Google Chrome!')
            cpath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(cpath)
            """

        elif 'tell me about' in query or 'what is' in query:
            speak("Wait,let me google that for you. Please be specific about what needs to be googled, it will fetch better results!")
            google_query=takeCommand().lower()
            webbrowser.open('https://www.google.co.in/search?q=' + google_query)

        elif 'define' in query or 'meaning of' in query:
            print('What is the word to be defined?')
            speak('What is the word to be defined?')
            word=takeCommand().lower()
            webbrowser.open("http://www.dictionary.com/cgi-bin/dict.pl?term=%s" % word)

        elif 'word of the day' in query:
            speak("Word of the day acoording to Dictionary.com is:")
            webbrowser.open("https://www.dictionary.com/e/word-of-the-day/")
            word_url='https://www.dictionary.com/e/word-of-the-day/'
            resp=requests.get(word_url) 
        
        elif 'send email' in query:
            try:
                speak('Please enter the email ID to which the mail has to be sent:')
                to_id=input('Enter the emailID:')

                speak('What should I say?')
                content=takeCommand()
                
                sendemail(to_id,content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                speak('Sorry, I couldnt do that for you. This happens rarely, umm how about we try this again?')
            
        elif 'inbox' in query:
            speak('Opening your Gmail!')
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

        elif 'weather' in query:
            speak('Opening google for you to check the weather!')
            webbrowser.open('https://www.google.com/search?rlz=1C1CHBF_enIN885IN885&sxsrf=ALeKk01N7JXe_0qA8dyjCexx1rM_6_DUhg%3A1590066498868&ei=Qn3GXrHRNN2D4-EPtviq2AM&q=weather+&oq=weather+&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIECAAQQzIICAAQgwEQkQIyBQgAEJECMgQIABBDMgoIABCDARAUEIcCMgIIADIKCAAQgwEQFBCHAjIECAAQQzoECAAQR1DGGFjGGGC3GmgAcAF4AIABkgGIAZIBkgEDMC4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwix-tWmg8XpAhXdwTgGHTa8CjsQ4dUDCAw&uact=5')

        elif 'about you' in query:
            speak('Soft Kitty, Warm Kitty, little ball of fur. Happy kitty, sleepy kitty, PURR, PURR, PURRR.')
            speak("hahaha BAZINGA")

        elif 'hi' in query or 'hey' in query or 'hello' in query:
            speak("Dont expect me to say How you doin?")
            speak("Now lets get back to work, enough chit chat")

        elif 'who made you' in query:
            speak("DUHH YOU DID! And for that, I Love you 3000!")
            speak("I really hope that was you Bhavana, dont want to say I love you to some worthless human being!")

        elif "bye" in query or "goodbye" in query or "see you" in query or "until next time" in query or "later" in query:
            speak('Alright! Until next time. Glad I could help!')
            sys.exit()
            
        
    

                


    