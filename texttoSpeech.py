from gtts import gTTS
import os
import pygame

def  texttoSpeech(cevap):

    pygame.mixer.init()
    # Text you want to convert to speech
    text = cevap

    # Language in which you want to convert
    language = 'tr'

    # Passing the text and language to the engine
    tts = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a file
    tts.save("./ses/output.mp3")

    # Playing the converted file
    # os.system("vlc output.mp3")
    pygame.mixer.music.load("./ses/output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)