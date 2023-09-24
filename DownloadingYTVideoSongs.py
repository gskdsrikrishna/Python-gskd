import youtube_dl

# Function to download a song from YouTube
def download_song(url):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

# Main program
url = input("Enter the YouTube URL of the song you want to download: ")
download_song(url)