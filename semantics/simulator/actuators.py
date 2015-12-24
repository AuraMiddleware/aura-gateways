import requests
import random
import urls
import helpers

def createContinuousActuator(actuatorIndex,variableIndex):
    actuatorId = helpers.actuatorIds[actuatorIndex]
    variable = helpers.variableIds[variableIndex]
    actuator = {
        "@context":urls.contextUrl + "continuousActuatorContext.jsonld",
        "@type":"ContinuousActuator",
        "@id":actuatorId,
        "actuator:increases":variable,
        "actuator:decreases":variable
    }

    return actuator

def createDiscreteActuator(actuatorIndex,variableIndex):
    actuatorId = helpers.actuatorIds[actuatorIndex]
    variable = helpers.variableIds[variableIndex]
    actuator = {
        "@context":urls.contextUrl + "discreteActuatorContext.jsonld",
        "@type":"DiscreteActuator",
        "@id":actuatorId,
        "actuator:changeState":variable
    }

    return actuator

def createActuators():
    for i in range(1):
        continuousActuator = createContinuousActuator(0,0)
        discreteActuator = createDiscreteActuator(1,1)
        requests.post(urls.globalManagerUrl+'actuators',None,continuousActuator)
        requests.post(urls.globalManagerUrl+'actuators',None,discreteActuator)

