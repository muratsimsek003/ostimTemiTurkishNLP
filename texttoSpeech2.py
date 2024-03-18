from gtts import gTTS
import io
import pygame
import streamlit as st
from streamlit_webrtc import (
    ClientSettings,
    WebRtcMode,
    webrtc_streamer,
)

def texttoSpeech(text):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Language in which you want to convert
    language = 'tr'

    # Passing the text and language to the engine
    tts = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a buffer
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_bytes = audio_buffer.getvalue()

    # Play the audio
    st.audio(audio_bytes, format='audio/mp3')

def main():
    st.title("Text to Speech with Streamlit")

    # Get text input from user
    text_input = st.text_input("Enter text to convert to speech:")

    # Play button to initiate text-to-speech conversion
    if st.button("Play"):
        texttoSpeech(text_input)

if __name__ == "__main__":
    main()
