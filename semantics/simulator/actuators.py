import semantics.simulator.urls as urls

def createContinuousActuator(id, url,variableId):
    actuator = {
        "id":id,
        "@context":urls.contextUrl + "continuousActuatorContext.jsonld",
        "@type":"ContinuousActuator",
        "@id":url + "continuous_actuators/" + id,
        "actuator:increases":url + "variables/" + variableId,
        "actuator:decreases":url + "variables/" + variableId
    }

    return actuator

def createDiscreteActuator(id, url,variableId):
    actuator = {
        "id":id,
        "@context":urls.contextUrl + "discreteActuatorContext.jsonld",
        "@type":"DiscreteActuator",
        "@id":url + "discrete_actuators/" + id,
        "actuator:changeState":url + "variables/" + variableId
    }

    return actuator
