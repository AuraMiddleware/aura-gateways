import paho.mqtt.client as mqtt
from time import sleep

from datetime import datetime
import random
import urls
import helpers

def createDevice(deviceID,platformIndex):
  device = {
    "@context": urls.contextUrl+"deviceContext.jsonld",
    "@type":"Device",
    "@id":deviceID,
    "dev:hasPlatform":helpers.platformIds[platformIndex]
  }

  return device

def createPlatform(platformIndex,sensorIndex,actuatorIndex):
    platformId = helpers.platformIds[platformIndex]
    platform = {
        "@context":urls.contextUrl+"platformContext.jsonld",
        "@type":"Platform",
        "@id":platformId,
        "brand":"Plataforma " + str(platformId),
        "dev:hasSensor":helpers.sensorIds[sensorIndex],
        "dev:hasActuator":helpers.actuatorIds[actuatorIndex]
    }
    #requests.post(urls.globalManagerUrl+'platforms',None,platform)


def createMeasurement(deviceId,coefficient):
    value = 10*coefficient
    id = helpers.localUrl + "measurements/measurement"+str(random.randint(0,1000))
    timestamp = str (datetime.now())
    measurement = {
        "@context":urls.contextUrl+"measurementContext.jsonld",
        "@type":"Measurement",
        "@id":id,
        "dev:wasMeasuredBy":deviceId,
        "value":value,
        "timestamp":timestamp
    }

    return measurement

def simulateDevices():
    #deviceUrl = urls.localManagerUrl + 'devices'
    #measurementUrl = urls.localManagerUrl + 'measurements'

    for i in range(20):
        index = i%2
        createPlatform(index,index,index)
        device = createDevice(helpers.deviceIdList[i],index)
        print (device)
        measurement = createMeasurement(helpers.deviceIdList[i],i)


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
    simulateDevices()

client.loop_stop()