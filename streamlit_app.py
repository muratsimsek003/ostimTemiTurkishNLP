# streamlit_app.py

import streamlit as st
import transformers
import pygame
import torch
import speechtoText
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
from texttoSpeech import texttoSpeech
from speechtoText import speechtoText
from gtts import gTTS
import time
import speech_recognition as sr
from temiturkishModel import temi_main


def main():
    st.title("OSTIMTECH TEMI")

    # Buton oluşturma
    button_clicked = st.button("BANA SORU SOR")
    if button_clicked:
        st.write("ŞİMDİ KONUŞARAK SORU SORABİLİRSİNİZ")
        temi_main()  # temiturkishModel.py dosyasındaki main fonksiyonunu çağır

if __name__ == "__main__":
    main()


#streamlit run streamlit_app.py

#(Created by Dr.Murat ŞİMŞEK)