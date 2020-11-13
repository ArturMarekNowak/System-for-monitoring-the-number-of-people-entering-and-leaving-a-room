import time
import paho.mqtt.client as mqtt


def establishConnection():
    
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print(f"Connected success, broker: broker.emqx.io, port: 1883, keepAlive: 60")
        else:
            print(f"Connected fail with code {rc}")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.emqx.io", 1883, 60)


def sendPicture(path, topic):
    
    f = open(path, "rb")
    fileContent = f.read()
    byteArr = bytes(fileContent)
    client.publish(topic, byteArr, qos = 0, retain = False)
    print(f"Picture from: {path}")
    print(f"Sent to topic: {topic}")
    client.loop_forever()

def sendNumber(number, topic):
    
    client.publish(topic, payload = number, qos = 0, retain = False)
    print(f"sent {number} to {topic}")
    client.loop_forever()
