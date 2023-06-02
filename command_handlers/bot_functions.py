import speech_recognition
from gtts import gTTS
from playsound import playsound
import random
import os

speechRecognition = speech_recognition.Recognizer()
speechRecognition.pause_threshold = 0.5

beepSound = "./assets/audio/beep.wav"
beepErrorSound = "./assets/audio/beep_error.wav"

# начало слушания
def listen():
    try:
        with speech_recognition.Microphone() as mic:
            speechRecognition.adjust_for_ambient_noise(source=mic, duration=0.5)
            print("Speak")
            playsound(beepSound)
            audio = speechRecognition.listen(source=mic)
            recognizedText = speechRecognition.recognize_google(audio_data=audio, language='ru-RU').lower()

            return recognizedText
    except speech_recognition.UnknownValueError:
        playsound(beepErrorSound)

# ответ помощника
def say(content):
    tts = gTTS(content, lang='ru')
    soundFile = f"{random.randint(0, 9999)}.mp3"
    tts.save(soundFile)
    playsound(soundFile)
    os.remove(soundFile)
    return soundFile