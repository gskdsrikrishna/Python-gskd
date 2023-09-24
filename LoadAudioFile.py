from pydub import AudioSegment
from pydub.playback import play

# Load audio file
audio = AudioSegment.from_file("audio_file.mp3", format="mp3")

# Play audio
play(audio)
