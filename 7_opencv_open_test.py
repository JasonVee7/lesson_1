import cv2

# Create a frame window
cv2.namedWindow('OpenCV Window', cv2.WINDOW_NORMAL)

# Access the webcam (change the index if you have multiple webcams)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = video_capture.read()

    # Display the captured frame in the window
    cv2.imshow('OpenCV Window', frame)

    # Check for the 'Esc' key to exit
    key = cv2.waitKey(1)
    if key == 27:  # 27 is the ASCII code for the 'Esc' key
        break

# Release the webcam and close the window
video_capture.release()
cv2.destroyAllWindows()
