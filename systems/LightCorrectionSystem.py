# File: systems/LightCorrectionSystem.py

from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port

# Replace enum with class constants
class CorrectionAction:
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    NONE = 0

class LightCorrectionSystem:
    def __init__(self, sensor_port: Port, reference_value=20, tolerance=5):
        """
        Initialize the correction system with a sensor, reference value, and tolerance.

        :param sensor_port: The port where the color sensor is connected.
        :param reference_value: Target light value (e.g., expected reflection level for the line).
        :param tolerance: Acceptable error range before action is needed.
        """
        self.sensor = ColorSensor(sensor_port)
        self.reference_value = reference_value
        self.tolerance = tolerance
        self.sensor_value = 0  # To store the latest sensor reading

    def process_input(self):
        """
        Read the sensor value, process it, and return a correction action and magnitude.

        :return: A tuple of (CorrectionAction, magnitude).
        """
        self.sensor_value = self.sensor.reflection()  # Get the reflection value

        error = self.sensor_value - self.reference_value

        if abs(error) <= self.tolerance:
            return CorrectionAction.NONE, 0

        magnitude = min(abs(error), 100)  # Ensure magnitude doesn't exceed 100

        if error > 0:
            # Sensor value is higher than the reference, meaning it's on lighter surface
            # Robot needs to move left to get back to the line
            return CorrectionAction.MOVE_LEFT, magnitude
        else:
            # Sensor value is lower than the reference, meaning it's on darker surface
            # Robot needs to move right to get back to the line
            return CorrectionAction.MOVE_RIGHT, magnitude