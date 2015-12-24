import requests
import random
import urls
import helpers

def createContinuousSensor(sensorId,index):
    sensor = {
        "@context":urls.contextUrl+"continuousSensorContext.jsonld",
        "@type":"ContinuousSensor",
        "@id":sensorId,
        "sense:canMeasure":createUnit(index),
        "precision":random.uniform(0.0,1.0),
        "minValue":0.0,
        "maxValue":100.0
    }

    return sensor

def createDiscreteSensor(sensorId,index):
    sensor = {
        "@context":urls.contextUrl+"discreteSensorContext.jsonld",
        "@type":"DiscreteSensor",
        "@id":sensorId,
        "sense:canMeasure":helpers.variableIds[index]
    }

    return sensor

def createUnit(index):
    unitId = helpers.globalUrl + "units/unit"+str(random.randint(0,1000))
    unit = {
        "@context":urls.contextUrl+"unitContext.jsonld",
        "@id":unitId,
        "@type":"Unit",
        "sense:unitOf":helpers.variableIds[index]
    }
    requests.post(urls.globalManagerUrl+'units',None,unit)

    return unitId

def createVariable(index):
    variableId = helpers.variableIds[index]
    variable = {
        "@context":urls.contextUrl+"variableContext.jsonld",
        "@id":variableId,
        "@type":"Variable"
    }
    requests.post(urls.globalManagerUrl+'variables',None,variable)


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
