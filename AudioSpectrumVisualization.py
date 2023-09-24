import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# Function to create the audio spectrum visualization
def create_audio_visualizer():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    fig, ax = plt.subplots()
    x = np.arange(0, CHUNK)
    line, = ax.plot(x, np.random.rand(CHUNK))

    ax.set_ylim(0, 255)
    ax.set_xlim(0, CHUNK)

    plt.xlabel('Frequency Bin')
    plt.ylabel('Magnitude')

    while True:
        data = stream.read(CHUNK)
        data_np = np.frombuffer(data, dtype=np.int16)

        line.set_ydata(np.abs(np.fft.fft(data_np))[:CHUNK] / CHUNK)

        plt.pause(0.001)
        ax.figure.canvas.draw()

    stream.stop_stream()
    stream.close()
    p.terminate()

# Main program
create_audio_visualizer()
