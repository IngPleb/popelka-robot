#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.tools import wait

import _thread
import time

from systems.LightSystem import LightSystem
from systems.LiftSystem import LiftSystem
from devices.SimpleUltraSonic import SimpleUltraSonic
from systems.DriveSystem import DriveSystem
from systems.GyroSystem import GyroSystem

light_port = Port.S1
ultra_sonic_port = Port.S2
gyro_sensor_port = Port.S3  # Assuming the gyro sensor is connected to port S3
lift_port = Port.D
lift_port = Port.D
ultra_sonic_port = Port.S2
left_motor_port = Port.A
right_motor_port = Port.C

def main():
    light_system = LightSystem(Port.S1, blue_threshold_on_line=7)
    ultra_sonic_sensor = SimpleUltraSonic(ultra_sonic_port, 140)
    lift_system = LiftSystem(lift_port)
    gyro_system = GyroSystem(gyro_sensor_port)
    drive_system = DriveSystem(
        left_motor_port=left_motor_port,
        right_motor_port=right_motor_port,
        wheel_diameter_mm=68.8,
        axle_track_mm=92.5,
        base_speed=200,
        correction_factor=7,  # Adjusted for combined gyro and light correction
        light_system=light_system,
        lift_system=lift_system,
        simple_ultra_sonic=ultra_sonic_sensor,
        gyro_system=gyro_system
    )

    drive_system.rotate_angle_gyro(81)
    while True:
         if drive_system.simple_ultra_sonic.is_object_in_front():
            print("Ball detected, initiating grab sequence.")
            time.sleep(0.42)
            _thread.start_new_thread(drive_system.lift_system.grab_without_return, ())

    


if __name__ == "__main__":
    main()
