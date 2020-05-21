# Virtual Personal Assistant
> Always wanted to have my personal assistant but the only way that could happen is 'virtually'. So here's a little fun project I made after binge watching The Big Bang Theory for the millionth time xD

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)

<p align="center"><img width=80% src="media/1..gif"></p>

## What can Sheldon do?
> Besides dropping 60 IQ points to call himself a genius, pretty much everything by automating tasks just by listening to you
1. Can recognize and respond to your voice commands (speech to text)
2. Google queries for you
3. Open and search YouTube
4. Open any required website
5. Summarize articles from wikipedia
6. Send an email for you
7. Define words according to dictionary.com and help with your vocabulary
8. Tell you about today's weather, the time and play music online
9. Greet you (I know that's not very Sheldon like!)

## Download Dependencies
```bash
pip install pyttsx3
pip install wikipedia
pip install smtplib
pip install urllib
pip install getpass
pip install speechRecognition
```
Importing Dependencies

```python
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
```

_This is just a weekend project though. It may not be perfect but it was super fun to make!_