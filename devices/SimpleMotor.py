import _thread

from pybricks.ev3devices import Motor
from pybricks.parameters import Port as Port, Stop


class SimpleMotor:
    def __init__(self, name, port: Port):
        self.name = name
        self.motor = Motor(port)
        self.motor.reset_angle(0)
        self.position = 0
        print("Motor {} initialized on port {}".format(self.name, port))

    def run(self, speed=500):
        self.motor.run(speed)

    def stop(self):
        self.motor.stop()

    def hold(self):
        self.motor.hold()

    def move_to_angle(self, angle, speed=500, wait: bool = True):
        self.position += angle

        # We are doing this to make sure the motor moves the exact number of degrees
        self.motor.run_angle(speed, angle, then=Stop.COAST, wait=wait)
        self.motor.reset_angle(0)
        self.motor.hold()
        print("Motor {} moved {} degrees".format(self.name, angle))

    def return_to_zero(self):
        # The return velocity can be higher than the move velocity
        self.move_to_angle(-self.position, speed=900)
        print("Motor {} returned to zero".format(self.name))
        self.position = 0

    def run_continuously(self, speed=500):
        _thread.start_new_thread(self.run, (speed,))
