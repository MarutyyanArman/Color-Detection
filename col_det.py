import cv2 as cv
import numpy as np

# Define a function that does nothing (it is used as a placeholder for trackbars)
def nothing(x):
    pass

# Open a video file or capture video from the webcam
# cap = cv.VideoCapture(0)  # Uncomment this to capture from webcam
cap = cv.VideoCapture("C:\\Users\\MSI\\Desktop\\Project\\Videos\\test_video.mp4")  # Comment this for webcam, use this for a video file

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame from BGR to HSV color space for better color detection
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Define lower and upper bounds for the color range to detect (in this case, blue)
    l_b = np.array([110, 50, 50])  # Lower bound of blue in HSV
    u_b = np.array([130, 255, 255])  # Upper bound of blue in HSV

    # Create a mask that highlights only the pixels within the specified color range
    mask = cv.inRange(hsv, l_b, u_b)

    # Apply the mask to the original frame, keeping only the pixels that fall within the color range
    res = cv.bitwise_and(frame, frame, mask=mask)

    # Display the original frame
    cv.imshow('video', frame)
    # Display the mask (shows white where the color is detected)
    cv.imshow('mask', mask)
    # Display the result (only the color detected areas)
    cv.imshow('res', res)

    # Wait for a key press for 1 ms; this helps with the video display
    cv.waitKey(1)

# Release the video capture object and close all windows when done
cap.release()
cv.destroyAllWindows()



