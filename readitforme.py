
# Purpose: Download web pages and read aloud visible text in specific CSS DIV elements.
# Author: P-C Markovski
# Version: 1.0


# Required modules for reading text aloud.
import pyttsx3

# Required modules for scraping web page data.
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

newVoiceRate = 130 # Set the speech rate.

engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice', voices[1].id)

# Speak text that is passed as text.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Scrape the web page data in div with class 'content-area'.
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    result = soup.find("div", {"class":"content-area"})
    return result




# Main program starts here.

# Open the URL and return object as context manager.
html = urllib.request.urlopen('https://www.europezigzag.com/2022/01/find-winter-sun-and-warmth-in-three-european-cities/').read()

# Prase the readable text in particular visual div element.
txt = text_from_html(html)
print(txt)


# Call the function read the text aloud.
speak(txt)
