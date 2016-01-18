import semantics.simulator.deviceSimulator as dev
import semantics.simulator.sense as sense
import semantics.simulator.actuators as act
import semantics.simulator.tasks as task

globalUrl = "http://localhost:5000/"

variableIds = ["continuousVariable","discreteVariable"]

unitIds = ["unit#1"]

continuousSensorIds = ["continuousSensor1"]
discreteSensorIds = ["discreteSensor1"]
sensorsIds = continuousSensorIds + discreteSensorIds

continuousActuatorIds = ["continuousActuator1"]
discreteActuatorIds = ["discreteActuator1"]
actuatorsIds = continuousActuatorIds + discreteActuatorIds

conditionValues = [5.44,55.7,40]

commandsIds = ["continuousCommand", "discreteCommand"]
conditionsIds = ["continuousCondition", "discreteCondition"]

platformIds = ["continuousPlatform1", "discretePlatform1"]

deviceIds = ["device" + str(x) for x in range(2)]


variables = {}
for i in range(len(variableIds)):
    variables[variableIds[i]] = sense.createVariable(variableIds[i],
                                                     globalUrl)

units = {}
for i in range(len(unitIds)):
    units[unitIds[i]] = sense.createUnit(unitIds[i], globalUrl, variableIds[i])

sensors = {}
for i in range(len(sensorsIds)):
    if i%2 == 0:
        sensors[sensorsIds[i]] = sense.createContinuousSensor(sensorsIds[i],
                                                              globalUrl,
                                                              unitIds[0])
    else:
        sensors[sensorsIds[i]] = sense.createDiscreteSensor(sensorsIds[i],
                                                            globalUrl,
                                                            variableIds[i])

actuators = {}
for i in range(len(actuatorsIds)):
    if i%2 == 0:
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
    if i%2 == 0:
        type = "continuous/"
    else:
        type = "discrete/"
    platforms[platformIds[i]] = dev.createPlatform(
        platformIds[i], globalUrl, "sensors/" + type + sensorsIds[i],
        "actuators/" + type + actuatorsIds[i])

devices = {}
for i in range(len(deviceIds)):
    devices[deviceIds[i]] = dev.createDevice(deviceIds[i],globalUrl,
                                             platformIds[i%2])
