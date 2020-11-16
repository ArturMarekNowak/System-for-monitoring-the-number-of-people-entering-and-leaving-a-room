import cv2
import imutils
import time
import sys
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected succesfully")
    else:
        print(f"Connection fail with error code: {rc}")

counter = 5
cascadePath = f"haarCascades/HS.xml"

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)

print("Start")

for i in range(12):
    
     
    path = f"docs/img{i}.jpg"
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascadePath)
    faces = cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        counter += 1
    print(counter)
    img = cv2.resize(img, (240, 120))
    cv2.imwrite("output/output.jpg", img)
    #cv2.imshow('imgae', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    time.sleep(1.0)
    f = open(f"output/output.jpg", "rb")
    fileContent = f.read()
    byteArr = bytes(fileContent)
    client.publish("raspberry/topic", counter, qos = 2, retain = True)
    #client.publish("raspberry/topic", byteArr, qos = 0, retain = True)
    counter = 0
    

    time.sleep(30)



client.loop_forever()
