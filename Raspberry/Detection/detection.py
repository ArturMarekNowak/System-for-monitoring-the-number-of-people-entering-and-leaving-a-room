from sys import argv

script, mode = argv

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
    cascadePath = r'HaarCascades/haarcascade_frontalface_default.xml'
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

    '''
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))

    time.sleep(0.1)



    face_cascade =  cv2.CascadeClassifier('/home/pi/Downloads/haarcascade_frontalface_default.xml')
    
    with picamera.PiCamera() as camera:
        stream = io.BytesIO()
    
        for foo in camera.capture_continuous(stream, format='jpeg'):
    	
	    for frame in camera.capture_continuous(rawCapture, format="bgr",  use_video_port=True):

    		img=np.asarray(frame.array)
    		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    		for (x,y,w,h) in faces:
        	    img = cv2.Rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    
        	    roi_gray = gray[y:y+h, x:x+w]
        	    roi_color = img[y:y+h, x:x+w]
     
	    # Truncate the stream to the current position (in case
            # prior iterations output a longer image)
            stream.truncate()
            stream.seek(0)
            if process(stream):
                break

    '''
    ''' 
    from picamera.array import PiRGBArray
    import picamera
    from imutils.object_detection import non_max_suppression
    import numpy as np
    import time
    import cv2
    mport imutils
    
    
    stream = io.BytesIO()
    
    with picamera.PiCamera() as camera: 
        camera.resolution(320, 240)
        camera.capture(stream, format = 'jpeg')

    buff = np.fromstring(stream.getvalue(), dtype = np.uint8)

    image = cv2.imdecode(buff, 1)

    face_cascade = cv2.CascadeClassifier(r"/home/pi/Inzynierka/Raspberry/HaarCascades")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2ARRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print "Found " + str(len(faces)) + " face(s)"
    
    for(x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Video", image)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    '''


            #haar_cascade_1 = cv2.CascadeClassifier(r"HaarCascades/haarcascade_upperbody.xml")

    # Uncomment this for real-time webcam detection
    # If you have more than one webcam & your 1st/original webcam is occupied,
    # you may increase the parameter to 1 or respectively to detect with other webcams, depending on which one you wanna use.

    '''
            camera = PiCamera()
            camera.resolution = (320, 240)
            camera.framerate = 16

            rawCapture = PiRGBArray(camera, size=(320, 240))
            time.sleep(0.1)

            for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

                img = np.array(frame.array)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                casc1 = haar_cascade_1.detectMultiScale(gray, 1.3, 5)

        # Draw a rectangle around the upper bodies
                for (x, y, w, h) in casc1:
                    img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1) 
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = color[y:y+h, x:x+w]

            #camera.truncate(0)
            #camera.seek(0)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

            cv2.imshow('Video', img) # Display video
            stream.truncate()
            stream.seek(0)
            
            if process(stream):
                break
        
        # Release capture
        video_capture.release()
        cv2.destroyAllWindows()
    '''

else:
    
    if mode[-4:] == ".avi":
        path = "Resources\\" + mode 
        print "loaded movie file: %s" % path
    elif mode[-4:] == ".jpg":
        path = "Resources\\" + mode
        print "loaded pic file: %s" % path



