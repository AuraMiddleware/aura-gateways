from datetime import datetime

import random
import semantics.simulator.urls as urls

def createDevice(id, url, platformId):
  device = {
    "id":id,
    "@context": urls.contextUrl + "deviceContext.jsonld",
    "@type":"Device",
    "@id":url + "devices/" + id,
    "dev:hasPlatform":url + "platforms/" + platformId
  }

  return device

def createPlatform(id, url, specific_sensor, specific_actuator):
    platform = {
        "id":id,
        "@context": urls.contextUrl + "platformContext.jsonld",
        "@type":"Platform",
        "@id":url + "platforms/" + id,
        "brand":"Plataforma " + id,
        "dev:hasSensor":url + specific_sensor,
        "dev:hasActuator":url  + specific_actuator
    }
    return platform

def createMeasurement(url, deviceId, variableId, value):
    timestamp = str (datetime.now())
    id = str(random.randint(0,10000)) + str(datetime.now().microsecond) +\
        str(random.randint(0,10000))
    measurement = {
        "id": id,
        "@context": urls.contextUrl + "measurementContext.jsonld",
        "@type": "Measurement",
        "@id": url + "measurements/" + id,
        "dev:wasMeasuredBy": url + "devices/" + deviceId,
        "dev:valueOf": url + "devices/" + variableId,
        "value": value,
        "timestamp": timestamp
    }

    return measurement