from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from systems.LightSystem import LightSystem

light_system = LightSystem(Port.S1, blue_threshold_on_line=7)

class SimpleUltraSonic:
    def __init__(self, port: Port, object_in_front_distance: int):
        self.name = "UltraSoundSensor"
        self.sensorDevice = UltrasonicSensor(port)
        self.object_inFront_distance = object_in_front_distance
        print("UltraSoundSensor initialized on port {}".format(port))

    def is_object_in_front(self):
        # print("Distance: {}".format(self.sensorDevice.distance()))
        return (self.sensorDevice.distance() <= self.object_inFront_distance or self.sensorDevice.distance() == 2550) or light_system.is_ball()

    def distance(self):
        return self.sensorDevice.distance()
