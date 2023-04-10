import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

image = cv2.imread('../img3.jpeg')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w, _ = image.shape
print(h, w)
result = face_mesh.process(rgb)
print(result)

for facial_landmarks in result.multi_face_landmarks:
    pt = facial_landmarks.landmark[28]
    x = pt.x*w
    y = pt.y*h
    print('x:', x, 'y:', y)

    cv2.circle(image, (int(x), int(y)), 2, (0, 0, 0), -1)


def show(title='Images', image=None, size=10):
    w, h = image.shape[0], image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize=(size*aspect_ratio, size))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


show('After face mesh', image)
