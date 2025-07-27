import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Words per minute
engine.setProperty('volume', 0.9)  # Max volume

sample_text = "Hello, I am your voice assistant. Let me describe the world to you."
engine.say(sample_text)
engine.runAndWait()
