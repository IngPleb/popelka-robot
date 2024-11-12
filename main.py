#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the EV3 Brick.

ev3 = EV3Brick()

# Motors
motor_A = Motor(Port.A)

motor_A.reset_angle(0)

motor_A.run_time(1000, 2000)

motor_A.run_time(-400, 1000)