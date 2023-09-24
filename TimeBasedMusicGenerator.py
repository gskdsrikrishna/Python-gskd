#Time-based Music Playlist Generator:
import datetime
import random

def generate_playlist():
    current_hour = datetime.datetime.now().hour

    if 6 <= current_hour < 12:
        playlist = ["Morning Vibes", "Happy Hits", "Energizing Tunes"]
    elif 12 <= current_hour < 18:
        playlist = ["Afternoon Mix", "Chill Out", "Feel Good"]
    elif 18 <= current_hour < 22:
        playlist = ["Evening Relaxation", "Dinner Party", "Soulful Sounds"]
    else:
        playlist = ["Late Night Beats", "Bedtime Chill", "Mellow Melodies"]

    random.shuffle(playlist)
    return playlist

playlist = generate_playlist()
print("Your suggested playlist:")
for i, song in enumerate(playlist, start=1):
    print(f"{i}. {song}")