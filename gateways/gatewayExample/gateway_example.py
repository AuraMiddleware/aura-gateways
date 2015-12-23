import paho.mqtt.client as mqtt
from time import sleep

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("gateways/broker")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    client.publish("gateways/test","test received:" + str(msg))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1885, 60)

client.loop_start()

while True:
    sleep(1)
    client.publish("gateways/test","i'm the gatewayExample!")

client.loop_stop()