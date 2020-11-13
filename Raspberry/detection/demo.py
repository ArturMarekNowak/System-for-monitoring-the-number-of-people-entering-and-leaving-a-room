import cv2
import imutils
import time
import sys
import paho.mqtt.client as mqtt


def onConnect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected succesfully")
    else:
        print(f"Connection fail with error code: {rc}")

counter = 0
cascadePath = f'haarCascades/HS.xml'

client = mqtt.Client()
print("xD")
client.on_connect = onConnect
print("xDD")
client.connect("broker.emqx.io", 1883, 60)
    
for i in range(12):
        
    path = f'docs/img{i}.jpg'
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascadePath)
    faces = cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        counter += 1
        
    print(counter)
    counter = 0
    cv2.imwrite('output.jpg', img)
    f = open('output.jpg', "rb")
    fileContent = f.read()
    byteArr = bytes(fileContent)
    client.publish('raspberry/topic', byteArr, qos = 0, retain = False)

        
        #cv2.imshow('image', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    
    time.sleep(15.0)

        
    if i == 11:
        i = 0

    client.loop_forever()
