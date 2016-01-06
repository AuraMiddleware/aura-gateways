globalUrl = "http://localhost:5000/"
localUrl = "http://localhost:5001/"

variableIds = [globalUrl+"variables/continuousVariable",
               globalUrl+"variables/discreteVariable"]

unitIds = [globalUrl+"units/unit#1"]

continuousSensorIds = [globalUrl+"sensors/continuousSensor#1"]
discreteSensorIds = [globalUrl+"sensors/discreteSensor#1"]
sensorsIds = continuousSensorIds + discreteSensorIds

continuousActuatorIds = [globalUrl+"actuators/continuousActuator#1"]
discreteActuatorIds = [globalUrl+"actuators/discreteActuator#1"]
actuatorsIds = continuousActuatorIds + discreteActuatorIds

scenarioValues = [5.44,55.7,40]

platformIds = [globalUrl+"platforms/continuousPlatform#1",
               globalUrl+"platforms/discretePlatform#1"]

deviceIds = [localUrl+"devices/device" + str(x) for x in range(2)]
