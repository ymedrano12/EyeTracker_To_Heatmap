import cv2

def preprocess_image(image):
    """Applies Gaussian blur and converts image to grayscale."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    return blurred
