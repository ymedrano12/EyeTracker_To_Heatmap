import cv2
import numpy as np
import csv
import time

# File to store gaze points
GAZE_FILE = "gaze_data.csv"

# Initialize file and write headers
with open(GAZE_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "x", "y"])  # Header

def detect_pupil(eye_gray, eye_color, frame, eye_x, eye_y):
    """Detects the pupil within an eye region and logs gaze coordinates."""
    _, thresh = cv2.threshold(eye_gray, 70, 255, cv2.THRESH_BINARY_INV)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    if contours:
        (cx, cy), radius = cv2.minEnclosingCircle(contours[0])
        cv2.circle(eye_color, (int(cx), int(cy)), int(radius), (255, 0, 0), 2)

        # Convert relative eye coordinates to screen coordinates
        screen_x = eye_x + int(cx)
        screen_y = eye_y + int(cy)

        # Save gaze coordinates to file
        with open(GAZE_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([time.time(), screen_x, screen_y])

        # Visual debug: Draw gaze point on full frame
        cv2.circle(frame, (screen_x, screen_y), 5, (0, 0, 255), -1)

    return eye_color
