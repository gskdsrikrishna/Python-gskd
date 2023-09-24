from moviepy.editor import ImageSequenceClip, concatenate_videoclips, TextClip, AudioFileClip

def create_slideshow(images, duration_per_image, transition_duration, music_path, captions=None):
    # Initialize a list to store the video clips
    video_clips = []

    # Iterate over the images
    for i, image in enumerate(images):
        # Create an ImageClip for each image
        image_clip = ImageSequenceClip([image], durations=[duration_per_image])

        # Add transition effects if not the first image
        if i != 0:
            transition_clip = image_clip.crossfadein(transition_duration)
            video_clips.append(transition_clip)

        # Add the image clip to the list
        video_clips.append(image_clip)

        # Add captions if provided
        if captions and i < len(captions):
            caption = captions[i]
            text_clip = TextClip(caption, fontsize=30, color='white').set_duration(duration_per_image)
            video_clips.append(text_clip)

    # Concatenate the video clips
    final_clip = concatenate_videoclips(video_clips)

    # Add background music if provided
    if music_path:
        audio_clip = AudioFileClip(music_path)
        final_clip = final_clip.set_audio(audio_clip)

    # Write the final video to a file
    final_clip.write_videofile("slideshow.mp4")

    print("Slideshow created successfully.")

def main():
    image_folder = input("Enter the folder path containing the images: ")
    duration_per_image = float(input("Enter the duration (in seconds) for each image: "))
    transition_duration = float(input("Enter the duration (in seconds) for the transition effect: "))
    music_path = input("Enter the path to the background music (leave blank for no music): ")

    # Load images from the folder
    images = [image_folder + '/' + image_name for image_name in os.listdir(image_folder)
              if image_name.endswith('.jpg') or image_name.endswith('.png')]

    # Generate slideshow
    create_slideshow(images, duration_per_image, transition_duration, music_path)

if __name__ == '__main__':
    main()
