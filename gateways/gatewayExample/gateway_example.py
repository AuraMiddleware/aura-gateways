import paho.mqtt.client as mqtt
from time import sleep
import json
import random
import semantics.simulator.deviceSimulator as dev
import semantics.simulator.helpers as helpers

collections = [helpers.devices, helpers.platforms, helpers.sensors,
               helpers.actuators, helpers.units, helpers.variables]
types = ['Device', 'Platform', 'Sensor', 'Actuator', 'Unit', 'Variable']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("gateways/broker")

def on_message(client, userdata, msg):
    obj = json.loads(msg.payload.decode())
    if obj['type'] in types:
        index = len(types) - 1
        while index >= types.index(obj['type']):
            print("index = " + str(index))
            for key in collections[index]:
                response = collections[index][key]
                #print("\n\nresponse:")
                #print(response)
                client.publish("gateways/test", json.dumps(response))
            index -= 1

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1885, 60)

client.loop_start()

index = 0
count = 1

print("deviceIds: " + str(len(helpers.deviceIds)))

while True:
    for id in helpers.devices:
        sleep(1)
        if index < len(helpers.unitIds):
            value = random.random() * 100
            variableId = helpers.variableIds[index]
        else:
            value = True
            variableId = helpers.variableIds[index]
        measurement = dev.createMeasurement(helpers.globalUrl,
                                            helpers.devices[id]["id"],
                                            helpers.variables[variableId]["id"],
                                            value)
        print(count)
        count += 1
        index += 1
        if index == len(helpers.deviceIds):
            index = 0
        client.publish("gateways/test", json.dumps(measurement))

client.loop_stop()