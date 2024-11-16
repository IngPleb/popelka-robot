# File: systems/LightCorrectionSystem.py

from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


class CorrectionAction:
    NONE = 0
    MOVE_LEFT = 1
    MOVE_RIGHT = 2


class LightCorrectionSystem:
    def __init__(self, sensor_port: Port, reference_value=20, tolerance=5):
        self.sensor = ColorSensor(sensor_port)
        self.reference_value = reference_value
        self.tolerance = tolerance
        self.previous_error = 0
        self.last_action = CorrectionAction.NONE

    def process_input(self):
        """
        Process the light sensor input and determine corrective actions.
        """
        # Get the current reflection value
        current_value = self.sensor.reflection()
        error = current_value - self.reference_value

        # If the error is within tolerance, no correction is needed
        if abs(error) <= self.tolerance:
            self.previous_error = error
            self.last_action = CorrectionAction.NONE
            return CorrectionAction.NONE, 0

        # Determine the magnitude of correction
        magnitude = min(abs(error), 100)

        # If the last action made things worse, reverse the correction
        if self.last_action == CorrectionAction.MOVE_LEFT and error > self.previous_error:
            self.last_action = CorrectionAction.MOVE_RIGHT
            self.previous_error = error
            return CorrectionAction.MOVE_RIGHT, magnitude
        elif self.last_action == CorrectionAction.MOVE_RIGHT and error < self.previous_error:
            self.last_action = CorrectionAction.MOVE_LEFT
            self.previous_error = error
            return CorrectionAction.MOVE_LEFT, magnitude

        # Otherwise, decide direction based on the error
        if error > 0:
            self.last_action = CorrectionAction.MOVE_LEFT
        else:
            self.last_action = CorrectionAction.MOVE_RIGHT

        self.previous_error = error
        return self.last_action, magnitude
