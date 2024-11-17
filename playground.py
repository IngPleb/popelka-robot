#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port
from systems.LiftSystem import LiftSystem

from systems.DriveSystem import DriveSystem
from systems.LightSystem import LightSystem

lift_port = Port.D


def main():
    light_system = LightSystem(Port.S1, blue_threshold_on_line=7)
    drive_system = DriveSystem(left_motor_port=Port.A, right_motor_port=Port.C, wheel_diameter_mm=68.8,
                               axle_track_mm=92.5,
                               base_speed=200, correction_factor=35, light_system=light_system,
                               lift_system=LiftSystem(lift_port))
    drive_system.move_distance(1250)
    #drive_system.move_distance_without_correction(500)
    #drive_system.rotate_angle(180)


if __name__ == "__main__":
    main()
