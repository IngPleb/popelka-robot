#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port

from devices.SimpleUltraSonic import SimpleUltraSonic
from systems.DriveSystem import DriveSystem
from systems.LiftSystem import LiftSystem
from systems.LightSystem import LightSystem

# Ports
#######################
# Sensors
light_port = Port.S1
lift_port = Port.D
ultra_sonic_port = Port.S2

# Motors
left_motor_port = Port.A
right_motor_port = Port.C


def main():
    # Initialize needed systems with Dependency Injection
    #######################
    light_system = LightSystem(light_port, blue_threshold_on_line=7)
    ultra_sonic_sensor = SimpleUltraSonic(ultra_sonic_port, 120)
    lift_system = LiftSystem(lift_port)
    drive_system = DriveSystem(left_motor_port=left_motor_port, right_motor_port=right_motor_port,
                               wheel_diameter_mm=68.8,
                               axle_track_mm=92.5,
                               base_speed=200, correction_factor=35, light_system=light_system,
                               lift_system=lift_system, simple_ultra_sonic=ultra_sonic_sensor)

    # Routine instructions
   # taking it from the other side of the map? anyways, after reaching the end of line, the last ball isn't collected yet, and we need to move a bit more (without correction, hence the 750T + 75F) and then it's a good idea to go back a bit for rotation
    # Four perpendicular lines from the main line




    # for i in range(4):
    #     # The distance is theoretically 840 mm
    #     # We will see based on the Adam's empirical data  (750 with correction + 75 without correction)
    #     drive_system.move_distance(840, True)
    #     drive_system.rotate_angle(180)
    #     # Returning back to the main line
    #     drive_system.move_distance(800, True)
    #     # We have noticed in earlier tests that the robot will make errors at crossing the perpendicular lines
    #     drive_system.move_distance(40, False)

    #     # Connecting to the main line
    #     drive_system.rotate_angle(90)  # TODO: find out if it is + or -  --> negative is counterclockwise
    #     drive_system.move_distance(280, False)
    #     drive_system.rotate_angle(-90)

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
