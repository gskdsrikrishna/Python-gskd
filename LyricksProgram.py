import requests

# Function to fetch and display song lyrics
def fetch_lyrics(artist, title):
    url = f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        lyrics = data.get("lyrics")
        if lyrics:
            print("Lyrics found:")
            print(lyrics)
        else:
            print("Lyrics not found for the given song.")
    else:
        print("Failed to fetch lyrics. Please try again.")

# Main program loop
while True:
    print("Lyrics Finder")
    print("1. Search Lyrics")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        artist = input("Enter the artist name: ")
        title = input("Enter the song title: ")
        fetch_lyrics(artist, title)
    elif choice == 2:
        break
    else:
        print("Invalid choice. Please try again.")