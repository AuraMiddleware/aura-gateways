import deviceSimulator
import sense
import actuators
import scenarios

sense.createSenseInfo()
actuators.createActuators()
scenarios.createScenarios()
deviceSimulator.simulateDevices()