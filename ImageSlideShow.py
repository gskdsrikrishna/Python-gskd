import tkinter as tk
from PIL import ImageTk, Image
import os

def image_slideshow(directory, duration=2000):
    images = []
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    current_index = 0

    def show_next_image():
        nonlocal current_index

        if current_index >= len(images):
            current_index = 0

        image_path = images[current_index]
        image = Image.open(image_path)
        image = image.resize((800, 600))  # Adjust the size as per your needs
        photo = ImageTk.PhotoImage(image)

        label.config(image=photo)
        label.image = photo

        current_index += 1
        root.after(duration, show_next_image)

    for file in os.listdir(directory):
        if os.path.splitext(file)[1].lower() in valid_extensions:
            images.append(os.path.join(directory, file))

    root = tk.Tk()
    label = tk.Label(root)
    label.pack()

    show_next_image()

    root.mainloop()

# Example usage
image_slideshow('D:/Py/', duration=3000)
