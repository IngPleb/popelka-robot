#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the EV3 Brick.

ev3 = EV3Brick()

# Motors
motor_A = Motor(Port.A)
motor_B = Motor(Port.B)

while True:
    motor_A.run(300)
    motor_B.run(300)
    wait(1000)
    motor_A.run(1000)
    motor_B.run(300)
    wait(1000)
