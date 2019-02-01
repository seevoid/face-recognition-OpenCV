import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
anterior = 0
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
    	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    	cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(faces):
    	anterior = len(faces)

    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()