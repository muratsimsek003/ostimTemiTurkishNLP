# temiturkishModel2.py

from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import sounddevice as sd
import soundfile as sf
from gtts import gTTS
import pygame

def texttoSpeech(cevap):
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
    pygame.mixer.music.load("./ses/output.mp3")
    pygame.mixer.music.play()

def record_audio(filename, duration, samplerate=44100):
    print("Kayıt başladı...")
    my_recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()
    sf.write(filename, my_recording, samplerate)
    print(f"Kayıt tamamlandı. Dosya: {filename}")

def play_audio(filename):
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    sd.wait()

def temi_main(os_question):
    # LOAD MODEL
    tokenizer = AutoTokenizer.from_pretrained("muratsimsek003/turkish_bert_qa")
    model = AutoModelForQuestionAnswering.from_pretrained("muratsimsek003/turkish_bert_qa")
    qa = pipeline("question-answering", model=model, tokenizer=tokenizer)

    with open('ostim.txt', encoding='utf-8') as dosya:
        ostim = dosya.read()

    cevap = qa(question=os_question, context=ostim)["answer"]
    texttoSpeech(cevap)
