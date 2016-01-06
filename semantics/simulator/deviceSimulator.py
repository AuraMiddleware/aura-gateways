from datetime import datetime

import random
import semantics.simulator.urls as urls
import semantics.simulator.helpers as helpers

def createDevice(deviceID,platformIndex):
  device = {
    "@context": urls.contextUrl + "deviceContext.jsonld",
    "@type":"Device",
    "@id":deviceID,
    "dev:hasPlatform":helpers.platformIds[platformIndex]
  }

  return device

def createPlatform(platformId,sensorId,actuatorId):
    platform = {
        "@context": urls.contextUrl + "platformContext.jsonld",
        "@type":"Platform",
        "@id":platformId,
        "brand":"Plataforma " + str(platformId),
        "dev:hasSensor":sensorId,
        "dev:hasActuator":actuatorId
    }
    return platform

def createMeasurement(deviceId,coefficient):
    value = coefficient
    id = helpers.localUrl + "measurements/measurement" + str(random.randint(0,1000))
    timestamp = str (datetime.now())
    measurement = {
        "@context": urls.contextUrl + "measurementContext.jsonld",
        "@type": "Measurement",
        "@id": id,
        "dev:wasMeasuredBy": deviceId,
        "value": value,
        "timestamp": timestamp
    }

    return measurement