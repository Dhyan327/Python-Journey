# In this part I will do "Exercise 9 Solution"
# Exercise :->
''' Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
    l = ["Rahul", "Nishant", "Harry"]

    Your program should pronouce:
    --> Shoutout to Rahul
    --> Shoutout to Nishant
    --> Shoutout to Harry
'''

# Solution :~~>
import time
names = ["Krunal", "Om", "Dhyan", "Dhyani", "Vishwa","Vrusti", "Vidita"]

# 1st Method (using pyttsx3 module):~~>
import pyttsx3
def text_to_speech(name):
    engine = pyttsx3.init()

    # You can set properties like volume and rate if needed
    engine.setProperty('rate', 150)         # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)       # Volume 0-1
    engine.say(f'Shoutout to {name}')
    engine.runAndWait()

print(f"Now, Shouting Out using pyttsx3 module")
for name in names:
    text_to_speech(name)
time.sleep(2)

# 2nd Method (using win32com.client module):~~>
import win32com.client
def speak(text, rate=1):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Rate = rate
    speaker.Speak(text)
print(f"Now, Shouting Out using win32com.client module")
for name in names:
    speak(f'Shoutout to {name}')
time.sleep(2)

# 3rd Method (using os module):~~>
import os
print(f"Now, Shouting Out using OS module")
for name in names:
    os.system(f'powershell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Shoutout to {name}\')"')