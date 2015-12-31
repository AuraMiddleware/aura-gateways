globalUrl = "http://localhost:5000/"
localUrl = "http://localhost:5001/"

variableIds = [globalUrl+"variables/continuousVariable",
               globalUrl+"variables/discreteVariable"]
sensorIds = [globalUrl+"sensors/continuousSensor",
             globalUrl+"sensors/discreteSensor"]
actuatorIds = [globalUrl+"actuators/continuousActuator",
               globalUrl+"actuators/discreteActuator"]
scenarioValues = [5.44,55.7,40]
platformIds = [globalUrl+"platforms/continuousPlatform",
               globalUrl+"platforms/discretePlatform"]
deviceIdList = [localUrl+"devices/device" + str(x) for x in range(20)]
