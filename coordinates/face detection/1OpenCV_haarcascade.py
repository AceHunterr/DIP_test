import cv2

img = cv2.imread('img1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(face_cascade_name)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    faces = img[y:y + h, x:x + w]
    cv2.imwrite('face.jpg', faces)

cv2.imwrite('detected.jpg', img)
cv2.waitKey()
