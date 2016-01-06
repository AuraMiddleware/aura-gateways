import paho.mqtt.client as mqtt
from time import sleep
import json
import random
import semantics.simulator.deviceSimulator as dev
import semantics.simulator.sense as sense
import semantics.simulator.actuators as act
import semantics.simulator.helpers as helpers

variables = {}
for i in range(len(helpers.variableIds)):
    variables[helpers.variableIds[i]] = sense.createVariable(
        helpers.variableIds[i])

units = {}
for i in range(len(helpers.unitIds)):
    units[helpers.unitIds[i]] = sense.createUnit(helpers.unitIds[i],
                                                 helpers.variableIds[i])

sensors = {}
for i in range(len(helpers.sensorsIds)):
    if i%2 == 0:
        sensors[helpers.sensorsIds[i]] = sense.createContinuousSensor(
            helpers.sensorsIds[i],
            helpers.unitIds[0]
        )
    else:
        sensors[helpers.sensorsIds[i]] = sense.createDiscreteSensor(
            helpers.sensorsIds[i],
            helpers.variableIds[i]
        )

actuators = {}
for i in range(len(helpers.actuatorsIds)):
    if i%2 == 0:
        actuators[helpers.actuatorsIds[i]] = act.createContinuousActuator(
            helpers.actuatorsIds[i],
            helpers.variableIds[i]
        )
    else:
        actuators[helpers.actuatorsIds[i]] = act.createDiscreteActuator(
            helpers.actuatorsIds[i],
            helpers.variableIds[i]
        )

platforms = {}
for i in range(len(helpers.platformIds)):
    platforms[helpers.platformIds[i]] = dev.createPlatform(
        helpers.platformIds[i], helpers.sensorsIds[i], helpers.actuatorsIds[i]
    )

devices = {}
for i in range(len(helpers.deviceIds)):
    devices[helpers.deviceIds[i]] = dev.createDevice(helpers.deviceIds[i],i%2)

measurements = {}

collections = [measurements, devices, platforms, sensors, actuators, units,
               variables]
types = ['Measurement', 'Device', 'Platform', 'Sensor', 'Actuator', 'Unit',
         'Variable']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("gateways/broker")

def on_message(client, userdata, msg):
    print(msg.payload.decode())
    obj = json.loads(msg.payload.decode())
    if obj['type'] in types:
        index = len(types) - 1
        while index >= 0:
            print("index = " + str(index))
            for key in collections[index]:
                response = collections[index][key]
                print("\n\nresponse:")
                print(response)
                client.publish("gateways/test",
                               json.dumps(response))
            index -= 1

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1885, 60)

client.loop_start()

index = 0
while True:
    for id in devices:
        sleep(1)
        if index%2 == 0:
            value = random.random() * 100
            index = 1
        else:
            value = True
            index = 0
        measurement = dev.createMeasurement(devices[id]["@id"], value)
        client.publish("gateways/test", json.dumps(measurement))

client.loop_stop()

