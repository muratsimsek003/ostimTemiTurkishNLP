import streamlit as st
from streamlit_webrtc import (
    ClientSettings,
    VideoTransformerBase,
    WebRtcMode,
    webrtc_streamer,
)
import speech_recognition as sr

class SpeechToTextTransformer(VideoTransformerBase):
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transform(self, frame):
        with sr.AudioData(frame.to_ndarray(format="wav"), sample_rate=frame.sample_rate) as audio_data:
            try:
                text = self.recognizer.recognize_google(audio_data, language="tr-TR")
                return text
            except sr.UnknownValueError:
                return "Üzgünüm, sesi anlayamadım."
            except sr.RequestError as e:
                return f"Üzgünüm, API isteği sırasında bir hata oluştu: {e}"

def main():
    st.title("Speech to Text with Streamlit")

    client_settings = ClientSettings(
        rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
        media_stream_constraints={"video": False, "audio": True},
    )

    webrtc_ctx = webrtc_streamer(
        key="speech-to-text",
        mode=WebRtcMode.SEND_ONLY,
        client_settings=client_settings,
        video_transformer_factory=SpeechToTextTransformer,
    )

    if webrtc_ctx.state.playing:
        st.success("Ses tanıma başladı. Lütfen konuşmaya başlayın...")

        text = webrtc_ctx.video_transformer_transform()
        st.write("Söylediğiniz: ", text)

if __name__ == "__main__":
    main()
