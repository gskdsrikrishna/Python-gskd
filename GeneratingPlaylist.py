import random

# Function to generate a playlist based on user preferences
def generate_playlist(preferred_genre, preferred_tempo):
    playlist = []
    for song in music_library:
        if song["genre"] == preferred_genre and song["tempo"] == preferred_tempo:
            playlist.append(song)
    return playlist

# Main program loop
music_library = [
    {"title": "Song 1", "artist": "Artist 1", "genre": "Genre 1", "tempo": "Slow"},
    {"title": "Song 2", "artist": "Artist 2", "genre": "Genre 2", "tempo": "Fast"},
    {"title": "Song 3", "artist": "Artist 3", "genre": "Genre 1", "tempo": "Medium"},
    {"title": "Song 4", "artist": "Artist 4", "genre": "Genre 3", "tempo": "Slow"},
    {"title": "Song 5", "artist": "Artist 5", "genre": "Genre 2", "tempo": "Medium"},
    {"title": "Song 6", "artist": "Artist 6", "genre": "Genre 3", "tempo": "Fast"},
    {"title": "Song 7", "artist": "Artist 7", "genre": "Genre 1", "tempo": "Medium"},
    {"title": "Song 8", "artist": "Artist 8", "genre": "Genre 2", "tempo": "Slow"},
    {"title": "Song 9", "artist": "Artist 9", "genre": "Genre 3", "tempo": "Fast"},
    {"title": "Song 10", "artist": "Artist 10", "genre": "Genre 1", "tempo": "Medium"}
]

while True:
    print("Music Playlist Generator")
    print("1. Generate Playlist")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        preferred_genre = input("Enter your preferred genre: ")
        preferred_tempo = input("Enter your preferred tempo (Slow, Medium, Fast): ")
        playlist = generate_playlist(preferred_genre, preferred_tempo)
        if playlist:
            print("Generated Playlist:")
            for song in playlist:
                print("Title:", song["title"])
                print("Artist:", song["artist"])
                print("-----------------------")
        else:
            print("No songs found with the given preferences.")
        print()
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")