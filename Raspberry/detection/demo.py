import cv2
import imutils
import time
import sys

counter = 0
cascadePath = f"haarCascades/HS.xml"

for i in range(12):
         
    path = f"docs/img{i}.jpg"
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascadePath)
    faces = cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        counter += 1
    #print(counter)
    img = cv2.resize(img, (240, 120))
    cv2.imwrite("output/output.jpg", img)
    #cv2.imshow('imgae', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    counter = 0
    

    time.sleep(10)



client.loop_forever()
