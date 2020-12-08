#Libraries
import cv2
import imutils
import time
import sys
from sys import argv
import json


#Input
name, mode = argv


#Update json
def updateJsonFile(counter, brightness, movement):
   
    data = {'firstSensor': {"Number of People": counter,
			    "Brightness": brightness,
			    "Movement": movement}}

    with open("detection/result.json", 'w') as jsonFile:
        json.dump(data, jsonFile, indent = 4)


#Brightness determination
def determineBrightness(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    return hsv[...,2].mean()


#Counter of people    
counter = 0

#Path to Haar Cascade
cascadePath = f"haarCascades/HS.xml"


#Input video
if mode[-4:] == ".mp4":
        
    #Path to videos
    path = "docs/" + mode
    
    #Capture video with cv2
    cap = cv2.VideoCapture(path)

    #Continuous frame capture 
    while True:
        
        #Read and determine brightness 
        success, img = cap.read()
        brightness = round(determineBrightness(img), 1)
        
        #Convert to grey, use cascade, count people, draw rectangles
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascadePath)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            counter += 1
        
        #Save image and update json file
        cv2.imwrite("output/output.jpg", img)
        updateJsonFile(counter, brightness, "No")

        #Show image
        #cv2.imshow("Video", img)
        
        #Interrupt 
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break

#Input demo mode
elif mode[-4:] == "demo":
    for i in range(12):
         
        #Path to pictures
        path = f"docs/img{i}.jpg"
        img = cv2.imread(path)
        
        #Determine brightness
        brightness = round(determineBrightness(img), 1)

        #Convert to grey, use cascade, count people, draw rectangles over person
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascadePath)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            counter += 1
        
        #Save to output and update json
        cv2.imwrite("output/output.jpg", img)
        updateJsonFile(counter, brightness, "No")
        
        #Reset counter, 10 second sleep
        counter = 0
        time.sleep(10)
    
