#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port

from devices.SimpleUltraSonic import SimpleUltraSonic
from systems.DriveSystem import DriveSystem
from systems.LiftSystem import LiftSystem
from systems.LightSystem import LightSystem
from systems.GyroSystem import GyroSystem

# Ports
#######################
# Sensors
light_port = Port.S1
ultra_sonic_port = Port.S2
gyro_sensor_port = Port.S3  # Assuming the gyro sensor is connected to port S3
lift_port = Port.D

# Motors
left_motor_port = Port.A
right_motor_port = Port.C

def main():
    # Initialize needed systems with Dependency Injection
    #######################
    light_system = LightSystem(light_port, blue_threshold_on_line=7)
    ultra_sonic_sensor = SimpleUltraSonic(ultra_sonic_port, 120)
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

    # Routine instructions
    #######################
    # Move along the line using combined gyro and light correction
    drive_system.move_distance(750)
    drive_system.move_distance(-850, use_correction=False)

    # Rotations
    drive_system.rotate_angle(-90)
    drive_system.move_distance(270, use_correction=False)
    drive_system.rotate_angle(90)

    drive_system.move_distance(750)
    drive_system.move_distance(-850, use_correction=False)

if __name__ == "__main__":
    main()