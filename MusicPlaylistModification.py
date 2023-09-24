import os

# Function to add a music file to the library
def add_song(library, file_path, artist, album, genre):
    song = {
        "file_path": file_path,
        "artist": artist,
        "album": album,
        "genre": genre
    }
    library.append(song)
    print("Song added successfully!")

# Function to remove a music file from the library
def remove_song(library, file_path):
    for song in library:
        if song["file_path"] == file_path:
            library.remove(song)
            print("Song removed successfully!")
            return
    print("Song not found in the library.")

# Function to search for music files by artist, album, or genre
def search_songs(library, key, value):
    found_songs = []
    for song in library:
        if song[key].lower() == value.lower():
            found_songs.append(song)
    if found_songs:
        print("Found Songs:")
        for song in found_songs:
            print("File Path:", song["file_path"])
            print("Artist:", song["artist"])
            print("Album:", song["album"])
            print("Genre:", song["genre"])
            print("----------------------")
    else:
        print("No songs found with the given criteria.")

# Main program loop
library = []

while True:
    print("1. Add Song")
    print("2. Remove Song")
    print("3. Search Songs")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        file_path = input("Enter the file path: ")
        artist = input("Enter the artist name: ")
        album = input("Enter the album name: ")
        genre = input("Enter the genre: ")
        add_song(library, file_path, artist, album, genre)
    elif choice == 2:
        file_path = input("Enter the file path of the song to remove: ")
        remove_song(library, file_path)
    elif choice == 3:
        print("Search Options:")
        print("1. Search by Artist")
        print("2. Search by Album")
        print("3. Search by Genre")
        search_choice = int(input("Enter your search choice: "))
        if search_choice == 1:
            artist = input("Enter the artist name: ")
            search_songs(library, "artist", artist)
        elif search_choice == 2:
            album = input("Enter the album name: ")
            search_songs(library, "album", album)
        elif search_choice == 3:
            genre = input("Enter the genre: ")
            search_songs(library, "genre", genre)
        else:
            print("Invalid search choice. Please try again.")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")

# Save the library to a text file before exiting
with open("music_library.txt", "w") as file:
    for song in library:
        file.write(f"{song['file_path']},{song['artist']},{song['album']},{song['genre']}\n")
