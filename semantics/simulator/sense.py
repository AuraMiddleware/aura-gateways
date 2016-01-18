import random
import semantics.simulator.urls as urls

def createContinuousSensor(id, url, unitId):
    sensor = {
        "id": id,
        "@context":urls.contextUrl+"continuousSensorContext.jsonld",
        "@type":"ContinuousSensor",
        "@id":url + "sensors/continuous/" + id,
        "sense:canMeasure":url + "units/" + unitId,
        "precision":random.uniform(0.0,1.0),
        "minValue":0.0,
        "maxValue":100.0
    }

    return sensor

def createDiscreteSensor(id, url, variableId):
    sensor = {
        "id":id,
        "@context":urls.contextUrl+"discreteSensorContext.jsonld",
        "@type":"DiscreteSensor",
        "@id":url + "sensors/discrete/" + id,
        "sense:canMeasure":url + "variables/" + variableId
    }

    return sensor

def createUnit(id, url, variableId):
    unit = {
        "id":id,
        "@context":urls.contextUrl+"unitContext.jsonld",
        "@id":url + "units/" + id,
        "@type":"Unit",
        "sense:unitOf":url + "variables/" + variableId
    }

    return unit

def createVariable(id, url):
    variable = {
        "id": id,
        "@context":urls.contextUrl+"variableContext.jsonld",
        "@id": url + "variables/" + id,
        "@type":"Variable"
    }

    return variable