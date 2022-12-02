# importing libraries to use in the program
import cv2

# initializing detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_defaults.xml')

# reading img
img = cv2.imread('test.jpg')

# converting into gray img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecting face
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h ) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255,0,0), 2)

# showing img
cv2.imshow('img', img)
cv2.waitkey()

# writing heading for the img
cv2.imwrite('face_detected.jpg', img)
