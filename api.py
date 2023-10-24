from gtts import gTTS
from playsound import playsound
import speech_recognition as sr


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Speech recognition request failed: {e}")

speech_to_text()
audio='speech.mp3'
language='en'
sp = gTTS(text="My name is krishnaveni",lang=language,slow=False)
sp.save(audio)
playsound(audio)