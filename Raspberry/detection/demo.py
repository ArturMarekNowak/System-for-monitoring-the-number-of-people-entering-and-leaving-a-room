import cv2
import imutils
import time
import sys
from sys import argv
import json

name, mode = argv


def updateJsonFile(counter, brightness, movement):
   
    data = {'firstSensor': {"Number of People": counter,
			    "Brightness": brightness,
			    "Movement": movement}}

    with open("detection/result.json", 'w') as jsonFile:
        json.dump(data, jsonFile, indent = 4)


def determineBrightness(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(hsv[...,2].mean())

    return hsv[...,2].mean()
    


with open("detection/result.json") as jsonFile:
    data = json.load(jsonFile)
    
    print(json.dumps(data, indent = 4))

    
counter = 0
cascadePath = f"haarCascades/HS.xml"

if mode[-4:] == ".mp4":
        
    path = "docs/" + mode
    print("loaded video file: %s" % path)

    cap = cv2.VideoCapture(path)

    while True:
        success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascadePath)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            counter += 1
        
        cv2.imshow("Video", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

elif mode[-4:] == "demo":
    for i in range(12):
         
        path = f"docs/img{i}.jpg"
        img = cv2.imread(path)
        brightness = determineBrightness(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascadePath)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            counter += 1
        
        cv2.imwrite("output/output.jpg", img)
        updateJsonFile(counter, brightness, "No")
        
        counter = 0
        time.sleep(30)
    
