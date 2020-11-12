import cv2
import imutils
import time

counter = 0

cascadePath = r'HaarCascades/HS.xml'

while True:
    
    for i in range(12):
        
        path = f"docs/img{i}.jpg"
        print(path)
        img = cv2.imread(path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascadePath)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for(x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            counter += 1
        
        print(counter)
        counter = 0
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
        #time.sleep(5.0)

        if i == 11:
            i = 0
