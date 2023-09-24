import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Create a function to play the music
def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# Create a function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Create a function to resume the music
def resume_music():
    pygame.mixer.music.unpause()

# Create a function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Create a function to adjust the volume
def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

# Main program loop
while True:
    print("1. Play Music")
    print("2. Pause Music")
    print("3. Resume Music")
    print("4. Stop Music")
    print("5. Adjust Volume")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        file = input("Enter the path of the music file: ")
        play_music(file)
    elif choice == 2:
        pause_music()
    elif choice == 3:
        resume_music()
    elif choice == 4:
        stop_music()
    elif choice == 5:
        volume = float(input("Enter the volume (0.0 to 1.0): "))
        set_volume(volume)
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")

# Quit Pygame mixer
pygame.mixer.quit()