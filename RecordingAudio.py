import sounddevice as sd
import soundfile as sf

# Set parameters for recording
duration = 5  # Recording duration in seconds
sample_rate = 44100  # Sample rate in Hz
channels = 2  # Number of audio channels

# Start recording
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)

# Wait for recording to complete
sd.wait()

# Save recording to a file
sf.write("recorded_audio.wav", recording, sample_rate)
