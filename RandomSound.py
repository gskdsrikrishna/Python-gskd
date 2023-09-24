from pydub import AudioSegment
import numpy as np
import random

def generate_random_sound(duration, sample_rate):
    num_samples = int(duration * sample_rate)
    samples = np.random.uniform(-1, 1, num_samples)  # Generating random samples between -1 and 1
    sound = AudioSegment(
        samples.tobytes(),
        frame_rate=sample_rate,
        sample_width=samples.dtype.itemsize,
        channels=1
    )
    return sound

# Example usage:
sound_duration = 5  # in seconds
sound_sample_rate = 44100  # standard sample rate for audio
random_sound = generate_random_sound(sound_duration, sound_sample_rate)
random_sound.export("random_sound.wav", format="wav")
