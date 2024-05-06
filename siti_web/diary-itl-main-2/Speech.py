import speech_recognition as sr

def speech():
    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        print("Si prega di parlare")
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        print("Conversione della voce in testo...")
        return recog.recognize_google(audio, language="it-IT")
