import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)
    
    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        return text.lower()
    except sr.UnknownValueError:
        return "Voice is incoherent. Unable to recognize speech."
    except sr.RequestError as e:
        return f"Error with the speech recognition service; {e}"

if __name__ == "__main__":
    spoken_text = recognize_speech()
    print("User Spoke : " + spoken_text)
    
    keywords = ["hello", "hi", "your custom keywords"]
    
    if any(keyword in spoken_text for keyword in keywords):
        print(spoken_text)
    else:
        print("Voice is incoherent. Unable to recognize specific speech.")
