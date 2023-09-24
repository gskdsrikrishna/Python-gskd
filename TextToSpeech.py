import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 0.8)  # Volume level

# Convert text to speech and save as an audio file
text = "Hello UPSC aspirants.How are you my name is Artificial Intelligence.I can provide a range of information to you.Good Bye"
engine.save_to_file(text, "text_to_speech.wav")

# Play back the generated speech
engine.say(text)
engine.runAndWait()