#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port

from systems.LiftSystem import LiftSystem

# Initialize the EV3 Brick.

ev3 = EV3Brick()

# Initialize the Motors

LiftMotorPort = Port.A


def main():
    # Initialize
    ev3.speaker.beep()

    lift_system = LiftSystem(LiftMotorPort)
    lift_system.grab()


if __name__ == "__main__":
    main()
