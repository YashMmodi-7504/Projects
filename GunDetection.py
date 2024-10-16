import numpy as np
import cv2
import imutils
import os

# Provide the correct absolute path to your cascade file
cascade_path = r'D:\msys64\GunDetection\GunDetection.py'  # Update this line with your file path

# Attempt to load the cascade
gun_cascade = cv2.CascadeClassifier(cascade_path)

# Verify cascade was loaded successfully
if gun_cascade.empty():
    print("Error loading cascade file. Check the file path and ensure it is a valid cascade file.")
    exit()

# Initialize the video capture
camera = cv2.VideoCapture(0)
firstFrame = None
gun_exist = False

while True:
    ret, frame = camera.read()

    if not ret:
        print("Error capturing video frame. Exiting.")
        break  # Exit the loop if no frame is captured

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns in the frame
    gun = gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100)
    )

    # If guns are detected, set the flag to True
    if len(gun) > 0:
        gun_exist = True

    # Draw rectangles around detected guns
    for (x, y, w, h) in gun:
        frame = cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0), 2
        )

    if firstFrame is None:
        firstFrame = gray
        continue

    # Display the video feed
    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

# Print the detection result
if gun_exist:
    print("Guns detected")
else:
    print("No guns detected")

# Release the video capture and close windows
camera.release()
cv2.destroyAllWindows()
