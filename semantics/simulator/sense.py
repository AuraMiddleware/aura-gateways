import requests
import random
import semantics.simulator.urls as urls
import semantics.simulator.helpers as helpers

def createContinuousSensor(sensorId, unitId):
    sensor = {
        "@context":urls.contextUrl+"continuousSensorContext.jsonld",
        "@type":"ContinuousSensor",
        "@id":sensorId,
        "sense:canMeasure":unitId,
        "precision":random.uniform(0.0,1.0),
        "minValue":0.0,
        "maxValue":100.0
    }

    return sensor

def createDiscreteSensor(sensorId, variableId):
    sensor = {
        "@context":urls.contextUrl+"discreteSensorContext.jsonld",
        "@type":"DiscreteSensor",
        "@id":sensorId,
        "sense:canMeasure":variableId
    }

    return sensor

def createUnit(unitId, variableId):
    unit = {
        "@context":urls.contextUrl+"unitContext.jsonld",
        "@id":unitId,
        "@type":"Unit",
        "sense:unitOf":variableId
    }

    return unit

def createVariable(variableId):
    variable = {
        "@context":urls.contextUrl+"variableContext.jsonld",
        "@id":variableId,
        "@type":"Variable"
    }

    return variable


def createSenseInfo():
    for i in range(1):
        createVariable(0)
        createVariable(1)
        continuousSensorId = helpers.sensorIds[0]
        discreteSensorId = helpers.sensorIds[1]
        continuousSensor = createContinuousSensor(continuousSensorId,0)
        discreteSensor = createDiscreteSensor(discreteSensorId,1)
        requests.post(urls.globalManagerUrl+'sensors',None,continuousSensor)
        requests.post(urls.globalManagerUrl+'sensors',None,discreteSensor)
