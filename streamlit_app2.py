# streamlit_app.py

import streamlit as st
from temiturkishModel2 import temi_main
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr


def record_and_convert_to_text():
    duration = 5  # Kayıt süresi
    filename = "user_input.wav"
    # Ses kaydı yap
    record_audio(filename, duration)
    # Ses dosyasını metne çevir
    text = convert_audio_to_text(filename)
    return text


def record_audio(filename, duration, samplerate=44100):
    st.write("Ses kaydı başlatıldı. Lütfen konuşun...")
    my_recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2)
    sd.wait()
    sf.write(filename, my_recording, samplerate)
    st.write("Ses kaydı tamamlandı.")


def convert_audio_to_text(filename):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(filename)
    with audio_file as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="tr-TR")
    return text


def main():
    st.title("OSTIMTECH TEMI")
    # Kenar çubuğu oluştur
    st.sidebar.image("logo.png", use_column_width=True)
    button_clicked = st.button("BANA SORU SOR")
    if button_clicked:
        st.write("ŞİMDİ KONUŞARAK SORU SORABİLİRSİNİZ")
        user_input_text = record_and_convert_to_text()
        st.write("Söylediğiniz: ", user_input_text)
        # temi_main(user_input_text)
        temi_response = temi_main(user_input_text)
        st.write("Sistemin Cevabı: ", temi_response)


if __name__ == "__main__":
    main()

#streamlit run streamlit_app2.py