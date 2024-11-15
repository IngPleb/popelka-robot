#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port

from systems.LiftSystem import LiftSystem
from systems.DriveSystem import DriveSystem

# Configuration
LIFT_MOTOR_PORT = Port.B
LEFT_MOTOR_PORT = Port.A
RIGHT_MOTOR_PORT = Port.D
COLOR_SENSOR_PORT = Port.S4

# Initialize the EV3 Brick
ev3 = EV3Brick()

def initialize_lift_system():
    lift_system = LiftSystem(LIFT_MOTOR_PORT)
    return lift_system

def initialize_drive_system():
    drive_system = DriveSystem(LEFT_MOTOR_PORT, RIGHT_MOTOR_PORT, COLOR_SENSOR_PORT)
    return drive_system

# In main.py - test sequence:
def main():
    ev3.speaker.beep()
    
    drive_system = DriveSystem(left_motor_port=Port.A, right_motor_port=Port.D, color_sensor_port=COLOR_SENSOR_PORT)
    
    print("Starting forward movement with correction...")
    drive_system.drive_forward_corrected_time(seconds=5, base_speed=200)
    
    print("Rotating...")
    drive_system.rotate(angle=90, speed=300)
    
    print("Program completed.")

        

if __name__ == "__main__":
    main()