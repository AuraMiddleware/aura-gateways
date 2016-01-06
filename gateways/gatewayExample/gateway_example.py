import paho.mqtt.client as mqtt
from time import sleep
import json

import semantics.simulator.deviceSimulator as dev
import semantics.simulator.sense as sense
import semantics.simulator.actuators as act
import semantics.simulator.helpers as helpers

variables = {}
for i in range(len(helpers.variableIds)):
    variables[helpers.variableIds[i]] = sense.createVariable(
        helpers.deviceIds[i])

units = {}
for i in range(len(helpers.unitIds)):
    units[helpers.unitIds[i]] = sense.createUnit(helpers.unitIds[i],
                                                 helpers.variableIds[i])

continuous_sensors = {}
for i in range(len(helpers.continuousSensorIds)):
    continuous_sensors[helpers.continuousSensorIds[i]] = \
        sense.createContinuousSensor(helpers.continuousSensorIds[i],
                                     helpers.variableIds[0])
discrete_sensors = {}
for i in range(len(helpers.continuousSensorIds)):
    discrete_sensors[helpers.discreteSensorIds[i]] = \
        sense.createDiscreteSensor(helpers.discreteSensorIds[i],
                                   helpers.variableIds[1])

continuous_actuators = {}
for i in range(len(helpers.continuousActuatorIds)):
        continuous_actuators[helpers.continuousActuatorIds[i]] = \
            act.createContinuousActuator(helpers.continuousActuatorIds[i],
                                         helpers.variableIds[0])

discrete_actuators = {}
for i in range(len(helpers.discreteActuatorIds)):
        discrete_actuators[helpers.discreteActuatorIds[i]] = \
            act.createDiscreteActuator(helpers.discreteActuatorIds[i],
                                         helpers.variableIds[1])

platforms = {}
platforms[helpers.platformIds[0]] = dev.createPlatform(
    helpers.platformIds[0], helpers.continuousSensorIds[0],
    helpers.continuousActuatorIds[0])
platforms[helpers.platformIds[1]] = dev.createPlatform(
    helpers.platformIds[1], helpers.discreteSensorIds[0],
    helpers.discreteActuatorIds[0])

devices = {}
for i in range(len(helpers.deviceIds)):
    devices[helpers.deviceIds[i]] = dev.createDevice(helpers.deviceIds[i],i%2)

measurements = {}

collections = [measurements, devices, platforms, continuous_actuators,
               discrete_actuators, continuous_sensors, discrete_sensors,
               units, variables]
types = ['Measurement', 'Device', 'Platform', 'ContinuousActuator',
         'DiscreteActuator', 'ContinuousSensor', 'DiscreteSensor', 'Unit',
         'Variable']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("gateways/broker")

def on_message(client, userdata, msg):
    print(msg.payload.decode())
    obj = json.loads(msg.payload.decode())
    if obj['type'] in types:
        response = collections[types.index(obj['type'])][obj['id']]
        print("\n\nresponse:")
        print(response)
        client.publish("gateways/test",
                       json.dumps(response))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1885, 60)

client.loop_start()

index = 0
while True:
    sleep(1)
    #dev.createPlatform(index,index,index)
    client.publish("gateways/test",
                  json.dumps(devices[helpers.deviceIds[(index%10)]]))
    index+=1


client.loop_stop()