#Libraries
import cv2
import imutils
import time
import sys
from sys import argv
import json
from imutils.object_detection import non_max_suppression
import numpy as np


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


#Input video to Haar
if mode[-4:] == "haar":
        
    #Path to videos
    path = "docs/vid1.mp4"
    
    #Capture video with cv2
    cap = cv2.VideoCapture(path)

    #Continuous frame capture 
    while True:
        
        #Read and determine brightness 
        success, img = cap.read()
        #img = cv2.resize(img, (120, 60))
        brightness = round(determineBrightness(img), 1)
        
        #Convert to grey, use cascade, count people, draw rectangles
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascadePath)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            counter += 1
        
        #Save image and update json file
        #cv2.imwrite("output/output.jpg", img)
        updateJsonFile(counter, brightness, "No")
        counter = 0 
        #Show image
        cv2.imshow("Video", img)
        
        #Interrupt 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#Input video to Hog
elif mode[-3:] == "hog":
        
    #Path to videos
    path = "docs/vid1.mp4"
    
    #Capture video with cv2
    cap = cv2.VideoCapture(path)
        
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    counter = 0

    #Continuous frame capture 
    while True:
        
        #Read and determine brightness 
        success, image = cap.read()
        brightness = round(determineBrightness(image), 1)
        
        (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale =1.05)

        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
            counter += 1

        cv2.imwrite("output/output.jpg", image)
        updateJsonFile(counter, brightness, "No")
        counter = 0
        #image = cv2.resize(image, (120, 60))
        #cv2.imshow("Vid", image)
        #key = cv2.waitKey(2) & 0xFF

        #if key == ord("q"):
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
    
