#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port

from systems.LiftSystem import LiftSystem
from systems.DriveSystem import DriveSystem

# Configuration
LIFT_MOTOR_PORT = Port.B
LEFT_MOTOR_PORT = Port.A
RIGHT_MOTOR_PORT = Port.D
COLOR_SENSOR_PORT = Port.S1

# Initialize the EV3 Brick
ev3 = EV3Brick()

def initialize_lift_system():
    lift_system = LiftSystem(LIFT_MOTOR_PORT)
    return lift_system

def initialize_drive_system():
    drive_system = DriveSystem(LEFT_MOTOR_PORT, RIGHT_MOTOR_PORT, COLOR_SENSOR_PORT)
    return drive_system

def main():
    try:
        ev3.speaker.beep()

        #lift_system = initialize_lift_system()
        #lift_system.grab()

        drive_system = initialize_drive_system()
        drive_system.drive_forward_corrected()
        drive_system.rotate(90)

    except Exception as e:
        for _ in range(3):
            ev3.speaker.beep()
        print("An error occurred: ", e)

if __name__ == "__main__":
    main()