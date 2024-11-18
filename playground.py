#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port

from devices.SimpleUltraSonic import SimpleUltraSonic
from systems.DriveSystem import DriveSystem
from systems.LiftSystem import LiftSystem
from systems.LightSystem import LightSystem

lift_port = Port.D


def main():
    light_system = LightSystem(Port.S1, blue_threshold_on_line=7)
    ultra_sonic_sensor = SimpleUltraSonic(Port.S2, 120)
    drive_system = DriveSystem(left_motor_port=Port.A, right_motor_port=Port.C, wheel_diameter_mm=68.8,
                               axle_track_mm=92.5,
                               base_speed=200, correction_factor=35, light_system=light_system,
                               lift_system=LiftSystem(lift_port), simple_ultra_sonic=ultra_sonic_sensor)
    drive_system.move_distance(750,True) # true for turn on the correction
    drive_system.move_distance(75,False)
    drive_system.move_distance(-25,False)
    # drive_system.move_distance_without_correction(500)
    drive_system.rotate_angle(-340)
    drive_system.move_distance(200,False)
    drive_system.move_distance(-50,False)
    drive_system.rotate_angle(-350)
    drive_system.move_distance(750,True)





if __name__ == "__main__":
    main()
