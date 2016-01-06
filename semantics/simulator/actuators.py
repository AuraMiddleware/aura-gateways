import requests
import random
import semantics.simulator.urls as urls
import semantics.simulator.helpers as helpers

def createContinuousActuator(actuatorId,variableId):
    actuator = {
        "@context":urls.contextUrl + "continuousActuatorContext.jsonld",
        "@type":"ContinuousActuator",
        "@id":actuatorId,
        "actuator:increases":variableId,
        "actuator:decreases":variableId
    }

    return actuator

def createDiscreteActuator(actuatorId,variableId):
    actuator = {
        "@context":urls.contextUrl + "discreteActuatorContext.jsonld",
        "@type":"DiscreteActuator",
        "@id":actuatorId,
        "actuator:changeState":variableId
    }

    return actuator

def createActuators():
    for i in range(1):
        continuousActuator = createContinuousActuator(0,0)
        discreteActuator = createDiscreteActuator(1,1)
        requests.post(urls.globalManagerUrl+'actuators',None,continuousActuator)
        requests.post(urls.globalManagerUrl+'actuators',None,discreteActuator)

