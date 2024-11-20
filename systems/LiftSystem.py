from pybricks.parameters import Port

from devices.SimpleMotor import SimpleMotor
from systems.System import System


class LiftSystem(System):
    GRAB_ANGLE = -700

    def __init__(self, port: Port):
        super().__init__("Lift System")
        self.simple_motor = SimpleMotor("Lift Motor", port)

    def grab(self):
        self.simple_motor.move_to_angle(LiftSystem.GRAB_ANGLE, speed=700)
        self.system_print("Grabbing a ball")
        self.simple_motor.return_to_zero()

    def grab_without_return(self):
        self.simple_motor.move_to_angle(LiftSystem.GRAB_ANGLE, speed=300)

    def run_continuously(self):
        self.simple_motor.run_continuously(speed=-1000)
