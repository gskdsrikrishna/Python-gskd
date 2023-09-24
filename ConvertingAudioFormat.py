from pydub import AudioSegment
import ffmpeg

# Convert audio format using Pydub
audio = AudioSegment.from_file("audio_file.mp3", format="mp3")
audio.export("output.wav", format="wav")

# Convert audio format using ffmpeg-python
input_file = "audio_file.mp3"
output_file = "output.wav"

ffmpeg.input(input_file).output(output_file).run()
