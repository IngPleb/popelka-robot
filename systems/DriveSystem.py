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
        """
        Drive forward with correction for a specified time.
        """
        start_time = time.time()
        correction_factor = 0.3  # Intensity of the correction

        try:
            while time.time() - start_time < seconds:
                # Get correction action and magnitude
                action, magnitude = self.correction_system.process_input()

                # Start with base speeds
                left_speed = base_speed
                right_speed = base_speed

                # Adjust speeds based on correction
                if action == CorrectionAction.MOVE_LEFT:
                    # Reduce right motor speed to turn left
                    right_speed = base_speed * (1 - correction_factor * (magnitude / 100))
                elif action == CorrectionAction.MOVE_RIGHT:
                    # Reduce left motor speed to turn right
                    left_speed = base_speed * (1 - correction_factor * (magnitude / 100))

                # Apply speeds to motors
                self.left_motor.motor.run(left_speed)
                self.right_motor.motor.run(right_speed)

                # Debugging logs
                print(
                    "Action: {}, Magnitude: {}, Left Speed: {}, Right Speed: {}".format(
                        action, magnitude, left_speed, right_speed
                    )
                )

                # Short delay to prevent overwhelming the system
                sleep(0.01)
        finally:
            # Stop motors after completing the movement
            self.left_motor.motor.stop()
            self.right_motor.motor.stop()