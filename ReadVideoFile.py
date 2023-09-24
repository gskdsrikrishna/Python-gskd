import cv2

# Read the video file
cap = cv2.VideoCapture('path/to/video/file.mp4')

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Break the loop if no frame is captured
    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video file and close the window
cap.release()
cv2.destroyAllWindows()
