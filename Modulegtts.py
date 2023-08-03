import speech_recognition as sr

r = sr.Recognizer()

# Set the device to be the default audio input device
with sr.Microphone() as source:
    print("Speak:")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error making request: {}".format(e))