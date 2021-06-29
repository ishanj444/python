# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 00:16:29 2020b

@author: jain
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
# pywhatkit.image_to_ascii_art('Capture.JPG', 'img2.txt')


# engine.say('how you doin')
engine.say('what can i do for you')
engine.runAndWait()

def talk(text):
     engine.say(text)
     engine.say('what else can i do for you')
     engine.runAndWait()
     
#def cui(text):
 #   engine.say(text)
  #  engine.say('what type of cuisine do u want')
   # engine.runAndWait()     

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'akira' in command:
                command = command.replace('akira','')
                #engine.say(command)
                #engine.runAndWait()
                #print(command)
                #talk(command)

    except:
        print('cannot hear you')
    return command

def run_bot():
    command = take_command()
    #print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'who is' in command:
        person = command.replace('who is','')
        #info = pywhatkit.info('virat kohli',1)
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'search' in command:
        find = command.replace('search','')
        talk('searching' + find)
        pywhatkit.search(find)
    elif 'cuisine' in command:
        find2 = command.replace('cuisine','')
        #cui('searching for the respective cuisine')
        print(find2)
        #print(find2)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'single' in command:
        talk('sorry , i am in a relationship with wifi')
    elif 'date' in command:
        talk('sorry , i am in a relationship with wifi')
    #elif 'convert image' in command:
     #   pywhatkit.image_to_ascii_art('x.JPG', 'y.txt')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please can you say the command again?')


#while True:
run_bot()