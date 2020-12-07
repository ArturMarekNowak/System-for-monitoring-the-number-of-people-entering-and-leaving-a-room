	
import io
import time
import picamera
import cv2
import numpy as np
import time
from picamera.array import PiRGBArray
from picamera import PiCamera    
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=(320, 240))

cascadePath = f"haarCascades/HS.xml"

faceCascade = cv2.CascadeClassifier(cascadePath)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE)

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 100), 1)
            
    cv2.imwrite(f'output/output.jpg', image)
    rawCapture.truncate(0)
    time.sleep(10)
