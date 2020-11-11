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

for i in range(5):
    client.publish('raspberry/topic', payload = i, qos = 0, retain = False)
    print(f"send {i} to raspberry/topic")
    time.sleep(i)


client.loop_forever()
