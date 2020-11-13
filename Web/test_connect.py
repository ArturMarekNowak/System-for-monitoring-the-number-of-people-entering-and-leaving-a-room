import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)


for i in range(4):
    
    f = open(f"../Raspberry/docs/lena{i}.jpg", "rb")
    fileContent = f.read()
    byteArr = bytes(fileContent)
    client.publish('raspberry/topic', byteArr, qos = 0, retain = False)
    print(f"lena{i} sent to raspberry/topic")
    time.sleep(10)


client.loop_forever()
