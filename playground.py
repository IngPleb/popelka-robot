#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port

from systems.DriveSystem import DriveSystem

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
    drive_system = DriveSystem(RIGHT_MOTOR_PORT, LEFT_MOTOR_PORT, COLOR_SENSOR_PORT)

    drive_system.drive_forward_corrected()


if __name__ == "__main__":
    main()
