#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port

from systems.LiftSystem import LiftSystem

# Initialize the EV3 Brick.

ev3 = EV3Brick()

# Define ports
###############

# Motors
RIGHT_MOTOR_PORT = Port.A
LEFT_MOTOR_PORT = Port.B

# Sensors
COLOR_SENSOR_PORT = Port.S1


def main():
    lift_system = LiftSystem(port=Port.D)
    lift_system.run_continuously()


if __name__ == "__main__":
    main()
