# File: systems/DriveSystem.py

import time
from time import sleep

from pybricks.parameters import Port

from devices.SimpleMotor import SimpleMotor
from systems.LightCorrectionSystem import LightCorrectionSystem, CorrectionAction
from systems.System import System


class DriveSystem(System):
    def __init__(self, left_motor_port: Port, right_motor_port: Port, color_sensor_port: Port):
        super().__init__("Drive System")
        self.left_motor = SimpleMotor("Left Drive", left_motor_port)
        self.right_motor = SimpleMotor("Right Drive", right_motor_port)
        self.correction_system = LightCorrectionSystem(color_sensor_port)

    def drive_forward_corrected_time(self, seconds: float, base_speed=200):
        """Drive forward with correction for specified time"""
        start_time = time.time()
        correction_factor = 0.3  # Adjust this value between 0 and 1 for correction intensity

        # Start motors
        self.left_motor.motor.run(base_speed)
        self.right_motor.motor.run(base_speed)

        try:
            while time.time() - start_time < seconds:
                action, magnitude = self.correction_system.process_input()

                left_speed = right_speed = base_speed

                if action == CorrectionAction.MOVE_LEFT:
                    # To move left, reduce speed of the left motor
                    left_speed = base_speed * (1 - correction_factor * (magnitude / 100))
                elif action == CorrectionAction.MOVE_RIGHT:
                    # To move right, reduce speed of the right motor
                    right_speed = base_speed * (1 - correction_factor * (magnitude / 100))
                # If action is NONE, both motors run at base_speed

                # Apply new speeds
                self.left_motor.motor.run(left_speed)
                self.right_motor.motor.run(right_speed)

                # Logging for debugging
                print("Action: {}, Magnitude: {}, Left Speed: {}, Right Speed: {}".format(action, magnitude, left_speed,
                                                                                          right_speed))

                sleep(0.01)  # Short delay for responsiveness
        finally:
            # Ensure motors stop after completion
            self.left_motor.motor.stop()
            self.right_motor.motor.stop()

    def rotate(self, angle: int, speed=300):
        """Rotate in place by given angle"""
        if angle > 0:
            # Rotate right
            self.left_motor.move(angle, speed=speed, wait=False)
            self.right_motor.move(-angle, speed=speed)
        else:
            # Rotate left
            self.left_motor.move(-angle, speed=speed, wait=False)
            self.right_motor.move(angle, speed=speed)
