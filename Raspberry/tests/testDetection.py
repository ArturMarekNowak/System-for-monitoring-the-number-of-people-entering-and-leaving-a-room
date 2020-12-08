import json
from sys import argv

script, mode = argv

cascadePath = r'haarCascades/HS.xml'

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


if mode[0] == "c":
    
    print("loaded cam")
    import io
    import time
    import picamera
    import cv2
    import numpy as np
    import time
    from picamera.array import PiRGBArray
    from picamera import PiCamera    
    import imutils
    import time
    import statistics
    camera = PiCamera()
    camera.resolution = (360, 240)
    camera.framerate = 36
    rawCapture = PiRGBArray(camera, size=(360, 240))

    time.sleep(5)

    faceCascade = cv2.CascadeClassifier(cascadePath)

    counter = 0
    avg = None

    firstFrame = None
    
    movementList = []
    counterList = []
    startTime = time.clock()
        
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        imageCopy = image
        
        brightness = determineBrightness(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        movement = 0

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE)
        
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if avg is None:
            avg = gray.copy().astype("float")
            rawCapture.truncate(0)
            continue

        cv2.accumulateWeighted(gray, avg, 0.5)
        frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        #print(cnts)
 

        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 100), 1)
                counter += 1
            #cv2.imwrite('detected.png',image)
            #os.remove("detected.png")
        
        counterList.append(counter)
       
        for c in cnts:
            
            if cv2.contourArea(c) < 250:
                continue
            
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            movement = 1
                #text = "Occupied"
        
        #cv2.imshow("Video", frame)
        
        movementList.append(movement)
        if (time.clock() - startTime) > 15:
            startTime = time.clock()
            counter = round(statistics.mean(counterList) , 0)
            movement = round(statistics.mean(movementList), 0)
            
            brightness = round(brightness, 1)

            if movement == 1:
                movement = "Yes"
            else:
                movement = "No"

            updateJsonFile(counter, brightness, movement)
            
            counterList = []
            movementList = []

        counter = 0
        
        cv2.imshow("Frame", image)	
        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

else:
    
    if mode[-4:] == ".mp4":
        import cv2
        import imutils
        
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

            cv2.imshow("Video", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    elif mode[-4:] == ".jpg":
        import cv2
        import imutils
        
        path = "docs/" + mode
        print("loaded pic file: %s" % path)

        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascadePath)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


