from pybricks.ev3devices import Motor
from pybricks.tools import wait


class DrivingSystem:
    def __init__(self, left_motor_port, right_motor_port, base_speed, correction_factor, light_correction_system):
        self.left_motor = Motor(left_motor_port)
        self.right_motor = Motor(right_motor_port)
        self.base_speed = base_speed
        self.correction_factor = correction_factor
        self.light_correction_system = light_correction_system

    def drive(self):
        while True:
            # Get correction from the LightCorrectionSystem
            correction = self.light_correction_system.get_correction()

            # Adjust motor speeds based on correction
            left_speed = self.base_speed - (correction * self.correction_factor)
            right_speed = self.base_speed + (correction * self.correction_factor)

            # Run motors with adjusted speeds
            self.left_motor.run(left_speed)
            self.right_motor.run(right_speed)

            # Add a small delay for control loop stability
            wait(10)
