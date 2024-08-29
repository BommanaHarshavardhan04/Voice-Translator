import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
recognizer = sr.Recognizer()
translator = Translator()
def translate_voice():
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            translated = translator.translate(text, dest='en')
            print(f"Translated Text: {translated.text}")
            tts = gTTS(translated.text, lang='te')
            tts.save("translated_audio.mp3")
            os.system("start translated_audio.mp3")  
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
if __name__ == "__main__":
    translate_voice()
