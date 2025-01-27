import cv2

def start_video_capture():
    """Initializes and returns the webcam video capture object."""
    cap = cv2.VideoCapture(0)  # 0 for default webcam
    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam.")
    return cap
