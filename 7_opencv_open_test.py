import cv2

# Create a frame window
cv2.namedWindow('OpenCV Window', cv2.WINDOW_NORMAL)

# Wait for the window to be closed
while True:
    key = cv2.waitKey(1)
    if key == 27:  # 27 is the ASCII code for the 'Esc' key
        break

# Close the window
cv2.destroyAllWindows()
