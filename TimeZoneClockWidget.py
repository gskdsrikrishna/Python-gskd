#Time Zone Clock Widget for Desktop:
import tkinter as tk
import datetime
import pytz

def update_clock(label):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    label.config(text=formatted_time)
    label.after(1000, lambda: update_clock(label))

root = tk.Tk()
root.title("Time Zone Clock Widget")

time_zones = ["America/New_York", "Europe/London", "Asia/Tokyo"]
labels = []

for i, tz in enumerate(time_zones):
    time_zone = pytz.timezone(tz)
    label = tk.Label(root, text="", font=("Arial", 24))
    label.grid(row=i, column=0, padx=10, pady=10)
    labels.append(label)

update_clock(labels[0])  # Update the first label immediately

for i in range(1, len(labels)):
    labels[i].after(i * 1000, lambda: update_clock(labels[i]))

root.mainloop()