from sys import argv

script, mode = argv

cascadePath = r'HaarCascades/HS.xml'
 
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
    camera = PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 16
    rawCapture = PiRGBArray(camera, size=(320, 240))

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
            #cv2.imwrite('detected.png',image)
            #os.remove("detected.png")

        cv2.imshow("Frame", image)	
        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

else:
    
    if mode[-4:] == ".mp4":
        import cv2
        import imutils
        
        path = "docs/" + mode
        print "loaded video file: %s" % path

        cap = cv2.VideoCapture(path)

        while True:
            success, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cascade = cv2.CascadeClassifier(cascadePath)
            faces = cascade.detectMultiScale(gray, 1.3, 5)
            for(x, y, w, h) in faces:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]

            cv2.imshow("Video", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        '''
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascadePath)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        cv2.imshow('video', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        '''

    elif mode[-4:] == ".jpg":
        import cv2
        import imutils
        
        path = "docs/" + mode
        print "loaded pic file: %s" % path

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


