#Capture the screen continuously and save it as a video:
import pyautogui
import cv2
import numpy as np

# Define the video codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_output = cv2.VideoWriter('screen_capture.mp4', fourcc, 30.0, (1920, 1080))

# Capture the screen continuously until the user interrupts
try:
    while True:
        # Capture the screen frame
        screenshot = pyautogui.screenshot()
        
        # Convert the screenshot to a numpy array
        frame = np.array(screenshot)
        
        # Convert BGR to RGB color format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Write the frame to the video file
        video_output.write(frame_rgb)
        
        # Display the resulting frame (optional)
        cv2.imshow('Screen Capture', frame_rgb)
        
        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) == ord('q'):
            break
finally:
    # Release the VideoWriter and destroy the OpenCV windows
    video_output.release()
    cv2.destroyAllWindows()