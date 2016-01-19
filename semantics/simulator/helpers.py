import semantics.simulator.deviceSimulator as dev
import semantics.simulator.sense as sense
import semantics.simulator.actuators as act

from random import random

globalUrl = "http://localhost:5000/"

variableIds = ["variable" + str(i) for i in range(1,51)]

unitIds = ["unit" + str(i) for i in range(1,26)]

continuousSensorIds = ["continuousSensor" + str(i) for i in range(1,26)]
discreteSensorIds = ["discreteSensor" + str(i) for i in range(1,26)]
sensorsIds = continuousSensorIds + discreteSensorIds

continuousActuatorIds = ["continuousActuator" + str(i) for i in range(1,26)]
discreteActuatorIds = ["discreteActuator" + str(i) for i in range(1,26)]
actuatorsIds = continuousActuatorIds + discreteActuatorIds

conditionValues = [random() + i for i in range(1,11)]

commandsIds = ["command" + str(i) for i in range(1,51)]
conditionsIds = ["condition" + str(i) for i in range(1,51)]

platformIds = ["platform" + str(i) for i in range(1,51)]

deviceIds = ["device" + str(x) for x in range(1,51)]


variables = {}
for i in range(len(variableIds)):
    variables[variableIds[i]] = sense.createVariable(variableIds[i],
                                                     globalUrl)

units = {}
for i in range(len(unitIds)):
    units[unitIds[i]] = sense.createUnit(unitIds[i], globalUrl, variableIds[i])


sensors = {}
for i in range(len(sensorsIds)):
    if i < len(unitIds):
        sensors[sensorsIds[i]] = sense.createContinuousSensor(sensorsIds[i],
                                                              globalUrl,
                                                              unitIds[i])
    else:
        sensors[sensorsIds[i]] = sense.createDiscreteSensor(sensorsIds[i],
                                                            globalUrl,
                                                            variableIds[i])


actuators = {}
for i in range(len(actuatorsIds)):
    if i < len(unitIds):
        actuators[actuatorsIds[i]] = act.createContinuousActuator(
            actuatorsIds[i],
            globalUrl,
            variableIds[i])
    else:
        actuators[actuatorsIds[i]] = act.createDiscreteActuator(actuatorsIds[i],
                                                                globalUrl,
                                                                variableIds[i])

platforms = {}
for i in range(len(platformIds)):
    if i < len(unitIds):
        type = "continuous/"
    else:
        type = "discrete/"
    platforms[platformIds[i]] = dev.createPlatform(
        platformIds[i], globalUrl, "sensors/" + type + sensorsIds[i],
        "actuators/" + type + actuatorsIds[i])

devices = {}
for i in range(len(deviceIds)):
    devices[deviceIds[i]] = dev.createDevice(deviceIds[i], globalUrl,
                                             platformIds[i])
