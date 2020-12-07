import time
import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")

def parseJsonFile():
    with open("detection/result.json", 'r') as jsonFile:
        data = json.load(jsonFile)
        numberOfPeople = data["firstSensor"]["Number of People"]
        brightness = data["firstSensor"]["Brightness"]
        movement = data["firstSensor"]["Movement"]
        return numberOfPeople, brightness, movement


client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)


while True:
    time.sleep(2)
    
    #f = open(f"output/output.jpg", "rb")
    #fileContent = f.read()
    #byteArr = bytes(fileContent)
    
    numberOfPeople, brightness, movement = parseJsonFile()
   
    client.publish('raspberry/numberOfPeople', numberOfPeople, qos = 0, retain = False)
    client.publish('raspberry/brightness', brightness, qos = 0, retain = False)
    client.publish('raspberry/movement', movement, qos = 0, retain = False)
    print(f"sent topics to raspberry")
    time.sleep(20)


client.loop_forever()
