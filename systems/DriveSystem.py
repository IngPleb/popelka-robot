from pybricks.ev3devices import Motor


class DrivingSystem:
    def __init__(self, left_motor_port, right_motor_port, base_speed, correction_factor, light_correction_system):
        self.left_motor = Motor(left_motor_port)
        self.right_motor = Motor(right_motor_port)
        self.base_speed = base_speed
        self.correction_factor = correction_factor
        self.light_correction_system = light_correction_system

    def drive(self):
        while True:
            blue_value = self.light_correction_system.color_sensor.rgb()[2]  # Get blue value
            correction = self.light_correction_system.get_correction()
            smoothed_correction = self.light_correction_system.get_smoothed_correction(correction)
            adjusted_correction = self.light_correction_system.adjust_correction(smoothed_correction, blue_value)

            left_speed = self.base_speed - (adjusted_correction * self.correction_factor)
            right_speed = self.base_speed + (adjusted_correction * self.correction_factor)

            self.left_motor.run(left_speed)
            self.right_motor.run(right_speed)
