import speech_recognition as sr


def speechtoText():
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Open a microphone input stream
        with sr.Microphone() as source:
            print("Lütfen konuşmaya başlayın...")  # Please start speaking...
            recognizer.adjust_for_ambient_noise(source)  # Arka plan gürültüsüne göre ayar yapın
            audio = recognizer.listen(source, timeout=5)  # En fazla 5 saniyelik sesi dinleyin

        # Recognize speech using Google Web Speech API
        try:
            print("Tanınıyor...")  # Recognizing...
            text = recognizer.recognize_google(audio, language="tr-TR")  # Türkçe tanıma için dil kodunu değiştirin
            print("Söylediğiniz:", text)  # You said:
        except sr.UnknownValueError:
            print("Üzgünüm, sesi anlayamadım.")  # Sorry, I could not understand the audio.
        except sr.RequestError as e:
            print(f"Üzgünüm, API isteği sırasında bir hata oluştu: {e}")  # Sorry, there was an error with the API request.
        return text