#!/usr/bin/env pybricks-micropython

from pybricks.parameters import Port

from systems.DriveSystem import DrivingSystem
from systems.LightCorrectionSystem import LightCorrectionSystem


def main():
    # Initialize the LightCorrectionSystem
    light_correction_system = LightCorrectionSystem(
        sensor_port=Port.S1,
        blue_threshold_on_line=7,
        blue_threshold_off_line=8,
        history_length=5
    )

    # Initialize the DrivingSystem with the LightCorrectionSystem
    driving_system = DrivingSystem(
        left_motor_port=Port.A,
        right_motor_port=Port.D,
        base_speed=300,  # Base speed for motors
        correction_factor=30,  # Sensitivity to corrections
        light_correction_system=light_correction_system
    )

    # Start the driving system
    driving_system.drive()


if __name__ == "__main__":
    main()
