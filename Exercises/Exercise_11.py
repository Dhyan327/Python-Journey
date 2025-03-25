# In this part I will do "Exercise 11 Solution"
# Exercise :->
''' Write a python program which reminds you of drinking water every hour or two. 
    Your program can either beep or send desktop notifications for a specific operating system
'''

# Solution :~~>
import os
import time

# 1st Method (using win10toast module) :~~>
from win10toast import ToastNotifier         # Note :~~> This Code will only run if the OS you are using is Windows 10, else it will not execute.

toast = ToastNotifier()
toast.show_toast(
    "Drink Water Reminder",
    "Hello Sir, Its time to drink water",
    duration = 5,
    threaded = True,
)
os.system(f'powershell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'Hello Sir, Its time to drink water\')"')


# 2nd Method (using plyer module):~~>
from plyer import notification

notification.notify(
title = "Drink Water Reminder",
message = "It's 1 hour! Please Drink Water",
timeout = 5
)
os.system(f'powershell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'please drink water!!\')"')


# 3rd Method (using win11toast module) :~~>
from win11toast import toast                # Note :~~> This Code will only run if the OS you are using is Windows 11, else it will not execute.

toast('Drink Water Reminder', 'Thank you')
os.system(f'powershell -Command "Add-Type -AssemblyName System.speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'....Thank you sir\')"')