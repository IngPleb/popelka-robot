from pybricks.parameters import Port

from systems.System import System
from devices.SimpleMotor import SimpleMotor


class LiftSystem(System):
    GRAB_ANGLE = -1670

    def __init__(self, port: Port):
        super().__init__("Lift System")
        self.simple_motor = SimpleMotor("Lift Motor", port)

    def grab(self):
        self.simple_motor.move(LiftSystem.GRAB_ANGLE, speed=700)
        self.system_print("Grabbing a ball")
        self.simple_motor.return_to_zero()
        
    def run_continuously(self):
        self.simple_motor.run_continuously(speed=-700)
