from pybricks.parameters import Port
from devices.SimpleMotor import SimpleMotor
from systems.System import System
from systems.LightCorrectionSystem import LightCorrectionSystem, CorrectionAction

class DriveSystem(System):
    def __init__(self, left_motor_port: Port, right_motor_port: Port, color_sensor_port: Port):
        super().__init__("Drive System")
        self.left_motor = SimpleMotor("Left Drive", left_motor_port)
        self.right_motor = SimpleMotor("Right Drive", right_motor_port)
        self.correction_system = LightCorrectionSystem(color_sensor_port)
        
    def drive_forward_corrected(self, base_speed=300):
        """Drive forward with light correction"""
        action, magnitude = self.correction_system.process_input()
        
        left_speed = right_speed = base_speed
        
        if action == CorrectionAction.MOVE_LEFT:
            # To move left, slow down left motor
            left_speed = base_speed - magnitude
        elif action == CorrectionAction.MOVE_RIGHT:
            # To move right, slow down right motor
            right_speed = base_speed - magnitude
        # If action is NONE, both motors run at base_speed
            
        self.left_motor.move(90, speed=left_speed)
        self.right_motor.move(90, speed=right_speed)
        
    def rotate(self, angle: int, speed=300):
        """Rotate in place by given angle"""
        if angle > 0:
            # Rotate right
            self.left_motor.move(angle, speed=speed)
            self.right_motor.move(-angle, speed=speed)
        else:
            # Rotate left
            self.left_motor.move(-angle, speed=speed)
            self.right_motor.move(angle, speed=speed)