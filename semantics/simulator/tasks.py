from semantics.simulator import urls
import requests
import json

def createCommand(id, url, value, variableId):
    command = {
        "id": id,
        "@context": urls.contextUrl + "commandContext.jsonld",
        "@type": "Command",
        "@id": url + "commands/" + id,
        "value": value,
        "task:enforces": url + "variables/" + variableId
    }

    return command

def createCondition(id, url, range1, range2, variableId, commandId):
    condition = {
        "id": id,
        "@context": urls.contextUrl + "conditionContext.jsonld",
        "@type": "Condition",
        "@id": url + "conditions/" + id,
        "minValue": range1,
        "maxValue": range2,
        "task:enforces": url + "variables/" + variableId,
        "task:triggers": url + "commands/" + commandId
    }

    return condition