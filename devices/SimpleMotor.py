from pybricks.ev3devices import Motor
from pybricks.parameters import Port as Port, Stop


class SimpleMotor:
    def __init__(self, name, port: Port):
        self.name = name
        self.motor = Motor(port)
        self.motor.reset_angle(0)
        self.position = 0
        print("Motor {} initialized on port {}".format(self.name, port))

    def move(self, angle, speed=500, wait: bool = True):
        self.position += angle

        # We are adding 3% to the angle to account for the motor not moving the exact number of degrees
        self.motor.run_angle(speed, angle, then=Stop.COAST, wait=wait)
        self.motor.reset_angle(0)
        self.motor.hold()
        print("Motor {} moved {} degrees".format(self.name, angle))

    def return_to_zero(self):
        """
        Moves the motor back to the zero position.

        This method moves the motor to the zero position by moving it in the 
        opposite direction of its current position at a speed of 900. After 
        the motor has returned to the zero position, it prints a message 
        indicating the motor has returned to zero and sets the position to 0.
        """
        # The return velocity can be higher than the move velocity
        self.move(-self.position, speed=900)
        print("Motor {} returned to zero".format(self.name))
        self.position = 0
        
    def run_continuously(self, speed = 500):
        while True:
            self.motor.run(speed)
            print("Motor {} running continuously".format(self.name))