#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port

from devices.SimpleUltraSonic import SimpleUltraSonic
from systems.DriveSystem import DriveSystem
from systems.LiftSystem import LiftSystem
from systems.LightSystem import LightSystem

# Ports
#######################
# Sensors
# light_port = Port.S1
lift_port = Port.D
ultra_sonic_port = Port.S2

# Motors
left_motor_port = Port.A
right_motor_port = Port.C


def main():
    # Initialize needed systems with Dependency Injection
    #######################
    # light_system = LightSystem(light_port, blue_threshold_on_line=7)
    lift_system = LiftSystem(lift_port)
    drive_system = DriveSystem(left_motor_port=left_motor_port, right_motor_port=right_motor_port,
                               wheel_diameter_mm=68.8,
                               axle_track_mm=92.5,
                               base_speed=400, correction_factor=29, light_system=None,
                               lift_system=lift_system, simple_ultra_sonic=None)

    # Routine instructions
    #######################
    # Make the lift spin perpetually
    lift_system.run_continuously()
    
    # Move along the perpendicular line
    # start with no correction so we make sure we are not on the cross
    #for i in range(2):
    #working at batt. lvl 7.07V

    drive_system.move_distance(730, True)
    drive_system.move_distance(-720, False)
    drive_system.rotate_angle(90)
    drive_system.move_distance(275, False)
    drive_system.rotate_angle(-94)
    drive_system.move_distance(770, True)
    
    drive_system.move_distance(-720, False)
    drive_system.rotate_angle(90)
    drive_system.move_distance(285, False)
    drive_system.rotate_angle(-94)
    drive_system.move_distance(770, True)

    drive_system.move_distance(-720, False)
    drive_system.rotate_angle(90)
    drive_system.move_distance(290, False)
    drive_system.rotate_angle(-94)
    drive_system.move_distance(770, True)
    
    drive_system.move_distance(-45, True)
    drive_system.rotate_angle(-96)
    drive_system.move_distance(-300, False)
    for i in range(4):
        drive_system.move_distance(20, False)
        drive_system.move_distance(-30, False)

    
    drive_system.move_distance(650, False)
    drive_system.rotate_angle(169)
    drive_system.move_distance(-400, False)
    for i in range(4):
        drive_system.move_distance(20, False)
        drive_system.move_distance(-30, False)

    # Adam's empirical data (we will use it for the adjusting the theoretical routine
    # drive_system.move_distance(750, True)  # true for turn on the correction
    # drive_system.move_distance(50, False)
    # drive_system.move_distance(-50, False)
    # drive_system.rotate_angle(-90)
    # drive_system.move_distance(300, False)
    # drive_system.move_distance(-50, False)
    # drive_system.rotate_angle(-90)
    # drive_system.move_distance(750, True)
    # drive_system.rotate_angle(90)
    # drive_system.move_distance(250, True)
    # drive_system.rotate_angle(90)
    # drive_system.move_distance(750, True)


if __name__ == "__main__":
    main()
