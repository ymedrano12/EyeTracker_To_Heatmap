import cv2
from video_capture import start_video_capture
from face_eye_detection import detect_faces_eyes
from pupil_tracking import detect_pupil
from utils import preprocess_image

def main():
    cap = start_video_capture()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame, face_data = detect_faces_eyes(frame)  # Detect faces and eyes

        for (x, y, w, h, eyes) in face_data:
            for (ex, ey, ew, eh) in eyes:
                eye_gray = preprocess_image(frame[y+ey:y+ey+eh, x+ex:x+ex+ew])
                eye_color = frame[y+ey:y+ey+eh, x+ex:x+ex+ew]
                detect_pupil(eye_gray, eye_color, frame, x+ex, y+ey)

        cv2.imshow('Eye Tracking System', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
