from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port

class GyroSystem:
    def __init__(self, sensor_port: Port):
        self.gyro_sensor = GyroSensor(sensor_port)
        self.gyro_sensor.reset_angle(0)
        print("GyroSensor initialized on port {}".format(sensor_port))

    def reset_angle(self):
        self.gyro_sensor.reset_angle(0)

    def get_angle(self):
        return self.gyro_sensor.angle()