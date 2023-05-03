#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 11:37:27 2023

@author: pothurinagasaisaketh
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said: ", text)
except:
    print("Sorry, I could not understand what you said.")
