from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port


class SimpleUltraSonic:
    def __init__(self, port: Port, object_inFront_distance: int):
        self.name = "UltraSoundSensor"
        self.sensorDevice = UltrasonicSensor(port)
        self.object_inFront_distance = object_inFront_distance
        print("UltraSoundSensor initialized on port {}".format(port))

    def is_object_in_front(self):
        print("Distance: {}".format(self.sensorDevice.distance()))
        return self.sensorDevice.distance() <= self.object_inFront_distance or self.sensorDevice.distance() == 2550
