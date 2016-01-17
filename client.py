import requests
from semantics.simulator import tasks, urls

commands_url = urls.global_url + "commands/"
conditions_url = urls.global_url + "conditions/"

condition1 = tasks.createCondition("condition1", urls.global_url, 20, 30,
                                   "continuousVariable")
condition2 = tasks.createCondition("condition2", urls.global_url, True, True,
                                   "discreteVariable")

command1 = tasks.createCommand("command1", urls.global_url, 25,
                               "continuousVariable")

command2 = tasks.createCommand("command2", urls.global_url, True,
                               "discreteVariable")


requests.post(commands_url, None, command1)
requests.post(commands_url, None, command2)
requests.post(conditions_url, None, condition1)
requests.post(conditions_url, None, condition2)