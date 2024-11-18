#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port

from devices.SimpleUltraSonic import SimpleUltraSonic

from systems.LiftSystem import LiftSystem
from systems.DriveSystem import DriveSystem
from systems.LightSystem import LightSystem

# Configuration
LEFT_MOTOR_PORT = Port.A
RIGHT_MOTOR_PORT = Port.C
COLOR_SENSOR_PORT = Port.S1
LIFT_PORT = Port.D

# Initialize the EV3 Brick
ev3 = EV3Brick()

def initialize_lift_system():
    lift_system = LiftSystem(LIFT_PORT)
    return lift_system

def initialize_drive_system():
    drive_system = DriveSystem(LEFT_MOTOR_PORT, RIGHT_MOTOR_PORT, COLOR_SENSOR_PORT)
    return drive_system

# In main.py - test sequence:
def main():
    ev3.speaker.beep()
    
    drive_system = DriveSystem(left_motor_port=Port.A, right_motor_port=Port.C, wheel_diameter_mm=68.8,
                               axle_track_mm=92.5,
                               base_speed=200, correction_factor=35, light_system=LightSystem,
                               lift_system=LiftSystem(LIFT_PORT), simple_ultra_sonic=SimpleUltraSonic)
    print("Starting forward movement with correction...")
    drive_system.move_distance(1250,True)
    
    print("Rotating...")
    drive_system.rotate(angle=90, speed=300)
    
    print("Program completed.")

        

if __name__ == "__main__":
    main()