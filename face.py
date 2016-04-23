import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    #cv2.imshow("photo",img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.3,
                                          minNeighbors=5
                                          )
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        subgray=gray[y:y+h, x:x+w]
        subface=image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(subgray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(subface,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	
	smiles = smile_cascade.detectMultiScale(subgray)
	for (ex,ey,ew,eh) in smiles:
            cv2.rectangle(subface,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
    cv2.imshow('face',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()








