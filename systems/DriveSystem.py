import time

from devices.SimpleMotor import SimpleMotor


class DriveSystem:
    def __init__(self, left_motor_port, right_motor_port, wheel_diameter_mm, axle_track_mm, base_speed,
                 correction_factor, light_system):
        # Initialize motors
        self.left_motor = SimpleMotor('left', left_motor_port)
        self.right_motor = SimpleMotor('right', right_motor_port)

        # Constants
        self.wheel_diameter_mm = wheel_diameter_mm
        self.axle_track_mm = axle_track_mm
        self.base_speed = base_speed
        self.correction_factor = correction_factor
        self.light_system = light_system

    def is_ball_detected(self):
        # TODO Placeholder for now; implement ball detection logic here
        return False

    def move_distance(self, distance_mm):
        print("Starting move_distance of " + str(distance_mm) + " mm")

        # Reset motor angles
        self.left_motor.motor.reset_angle(0)
        self.right_motor.motor.reset_angle(0)

        wheel_circumference = 3.1416 * self.wheel_diameter_mm
        target_angle = (distance_mm / wheel_circumference) * 360.0  # degrees

        # Start moving
        while True:
            # Get the average of the two motor angles
            left_angle = self.left_motor.motor.angle()
            right_angle = self.right_motor.motor.angle()
            average_angle = (left_angle + right_angle) / 2.0

            if average_angle >= target_angle:
                # Target distance reached
                break

            # Get correction from LightSystem
            correction = self.light_system.get_correction()
            # Adjust motor speeds
            left_speed = self.base_speed - (correction * self.correction_factor)
            right_speed = self.base_speed + (correction * self.correction_factor)

            # Set motor speeds
            self.left_motor.run(left_speed)
            self.right_motor.run(right_speed)

            # Debug statements
            print("Left angle: " + str(left_angle) + ", Right angle: " + str(right_angle) + ", Correction: " + str(
                correction))
            print("Left speed: " + str(left_speed) + ", Right speed: " + str(right_speed))

            # Check for ball detection
            if self.is_ball_detected():
                # For now, pass
                print("Ball detected, but not implemented yet.")
                pass

            # Small delay to prevent tight loop
            time.sleep(0.01)  # wait 10 ms

        # Stop motors
        self.left_motor.stop()
        self.right_motor.stop()
        print("move_distance completed.")

    def move_distance_without_correction(self, distance_mm, speed=None):
        if speed is None:
            speed = self.base_speed
        print("Starting move_distance_without_correction of " + str(distance_mm) + " mm")

        wheel_circumference = 3.1416 * self.wheel_diameter_mm
        rotation_angle = (distance_mm / wheel_circumference) * 360.0  # degrees

        # Move both motors forward by rotation_angle
        self.left_motor.move_to_angle(rotation_angle, speed, wait=False)
        self.right_motor.move_to_angle(rotation_angle, speed)

        print("move_distance_without_correction completed.")

    def rotate_angle(self, angle_degrees, speed=None):
        if speed is None:
            speed = self.base_speed
        print("Starting rotate_angle of " + str(angle_degrees) + " degrees")

        # Compute rotation distance
        rotation_circumference = 3.1416 * self.axle_track_mm
        rotation_distance_mm = (rotation_circumference * angle_degrees) / 360.0

        # Compute wheel rotation angle
        wheel_circumference = 3.1416 * self.wheel_diameter_mm
        wheel_rotation_angle = (rotation_distance_mm / wheel_circumference) * 360.0  # degrees

        # Use move_to_angle to move the motors
        self.left_motor.move_to_angle(wheel_rotation_angle, speed, wait=False)
        self.right_motor.move_to_angle(-wheel_rotation_angle, speed)

        print("rotate_angle completed.")
