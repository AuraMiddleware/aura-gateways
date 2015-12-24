import requests
import random
import urls
import helpers

def createDiscreteScenario(value,variableIndex):
    discreteScenarioId = helpers.globalUrl + "scenarios/discreteScenario"+\
                         str(random.randint(0,1000))
    discreteScenario = {
        "@context": urls.contextUrl + "discreteScenarioContext.jsonld",
        "@type":"DiscreteScenario",
        "@id":discreteScenarioId,
        "value":value,
        "scenario:enforces":helpers.variableIds[variableIndex]
    }
    requests.post(urls.globalManagerUrl+'scenarios',None,discreteScenario)

    return discreteScenario

def createContinuousScenario(range1,range2,variableIndex):
    continuousScenarioId = helpers.globalUrl + "scenarios/continuousScenario"+\
                           str(random.randint(0,1000))
    continuousScenario = {
        "@context":urls.contextUrl+"continuousScenarioContext.jsonld",
        "@type":"ContinuousScenario",
        "@id":continuousScenarioId,
        "minValue":helpers.scenarioValues[range1],
        "maxValue":helpers.scenarioValues[range2],
        "scenario:enforces":helpers.variableIds[variableIndex]
    }
    requests.post(urls.globalManagerUrl+'scenarios',None,continuousScenario)

    return continuousScenario

def createScenarios():
    discreteScenarioValue = helpers.scenarioValues[2]
    continuousScenario = createContinuousScenario(0,1,0)
    discreteScenario = createDiscreteScenario(discreteScenarioValue,1)
    requests.post(urls.globalManagerUrl+'scenarios',None,continuousScenario)
    requests.post(urls.globalManagerUrl+'scenarios',None,discreteScenario)