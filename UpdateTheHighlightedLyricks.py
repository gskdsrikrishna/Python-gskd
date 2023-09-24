import tkinter as tk
import time

# Function to update the highlighted lyrics
def update_lyrics(index):
    lyrics_label.config(text=lyrics[index], fg="red")
    lyrics_label.after(2000, lambda: update_lyrics(index + 1))

# Main program
lyrics = [
    "Oh, I've heard a thousand stories of what they think you're like",
    "But I've heard the tender whispers of love in the dead of night",
    "And you tell me that you're pleased and that I'm never alone",
    "You're a good, good Father",
    "It's who you are, it's who you are, it's who you are",
    "And I'm loved by you",
    "It's who I am, it's who I am, it's who I am"
]

window = tk.Tk()
window.title("Karaoke Application")
window.geometry("500x300")

lyrics_label = tk.Label(window, text="", font=("Arial", 16))
lyrics_label.pack(pady=20)

start_button = tk.Button(window, text="Start", font=("Arial", 12), command=lambda: update_lyrics(0))
start_button.pack(pady=10)

window.mainloop()