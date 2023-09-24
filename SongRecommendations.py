import random

# Function to generate random songs for demonstration purposes
def generate_songs():
    songs = [
        {"title": "Song 1", "artist": "Artist 1", "genre": "Genre 1"},
        {"title": "Song 2", "artist": "Artist 2", "genre": "Genre 2"},
        {"title": "Song 3", "artist": "Artist 3", "genre": "Genre 1"},
        {"title": "Song 4", "artist": "Artist 4", "genre": "Genre 3"},
        {"title": "Song 5", "artist": "Artist 5", "genre": "Genre 2"},
        {"title": "Song 6", "artist": "Artist 6", "genre": "Genre 3"},
        {"title": "Song 7", "artist": "Artist 7", "genre": "Genre 1"},
        {"title": "Song 8", "artist": "Artist 8", "genre": "Genre 2"},
        {"title": "Song 9", "artist": "Artist 9", "genre": "Genre 3"},
        {"title": "Song 10", "artist": "Artist 10", "genre": "Genre 1"}
    ]
    return songs

# Function to recommend similar songs based on genre
def recommend_songs(songs, user_song):
    recommended_songs = []
    for song in songs:
        if song["genre"] == user_song["genre"] and song != user_song:
            recommended_songs.append(song)
    return recommended_songs

# Main program loop
songs = generate_songs()

while True:
    print("Music Recommendation System")
    print("1. Get Song Recommendations")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        user_song = random.choice(songs)
        print("User Song:", user_song["title"])
        print("Artist:", user_song["artist"])
        print("Genre:", user_song["genre"])
        print("-----------------------")
        recommended_songs = recommend_songs(songs, user_song)
        if recommended_songs:
            print("Recommended Songs:")
            for song in recommended_songs:
                print("Title:", song["title"])
                print("Artist:", song["artist"])
                print("-----------------------")
        else:
            print("No recommendations found for the given song.")
        print()
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")
