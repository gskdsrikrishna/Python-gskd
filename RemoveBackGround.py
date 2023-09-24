import cv2
from moviepy.editor import VideoFileClip

def remove_background(video_path, output_path, background_path=None):
    # Load the video
    video = VideoFileClip(video_path)

    # Extract frames from the video
    frames = []
    for frame in video.iter_frames():
        frames.append(frame)

    # Apply background subtraction to each frame
    bg_subtracted_frames = []
    for frame in frames:
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply background subtraction
        _, mask = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)

        # Invert the mask
        mask_inv = cv2.bitwise_not(mask)

        # Apply the mask to the frame
        bg_removed_frame = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # Append the background removed frame
        bg_subtracted_frames.append(bg_removed_frame)

    # Create a new video from the processed frames
    processed_video = VideoFileClip(video_path).set_duration(len(bg_subtracted_frames) / video.fps)
    processed_video = processed_video.fl(lambda i: bg_subtracted_frames[i])

    # If a custom background is provided, replace the video background
    if background_path:
        background_video = VideoFileClip(background_path).resize(height=video.size[1])
        final_video = processed_video.set_mask(background_video.mask).set_duration(background_video.duration)
    else:
        final_video = processed_video

    # Write the final video to a file
    final_video.write_videofile(output_path, codec='libx264')

    print("Background removal completed successfully.")

def main():
    video_path = input("Enter the path to the video file: ")
    output_path = input("Enter the output path for the processed video: ")
    background_path = input("Enter the path to the custom background (leave blank for green screen effect): ")

    remove_background(video_path, output_path, background_path)

if __name__ == '__main__':
    main()