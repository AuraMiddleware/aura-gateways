from semantics.simulator import urls

def createCommand(id, url, value,variableId):
    command = {
        "id":id,
        "@context": urls.contextUrl + "discreteScenarioContext.jsonld",
        "@type":"DiscreteScenario",
        "@id":url + "commands/" + id,
        "value":value,
        "scenario:enforces":url + "variables/" + variableId
    }

    return command

def createCondition(id, url, range1, range2, variableId):
    condition = {
        "id":id,
        "@context":urls.contextUrl+"continuousScenarioContext.jsonld",
        "@type":"ContinuousScenario",
        "@id":url + "conditions/" + id,
        "minValue":range1,
        "maxValue":range2,
        "scenario:enforces":url + "variables/" + variableId
    }

    return condition
