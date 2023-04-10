import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

img = cv2.imread('img2.jpg')
with mp_face_detection.FaceDetection(
        model_selection=1, min_detection_confidence=0.5) as face_detection:
    image = img.copy()
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    annotated_image = image.copy()
    for detection in results.detections:
        mp_drawing.draw_detection(annotated_image, detection)
    cv2.imwrite('annotated_image1.jpg', annotated_image)
