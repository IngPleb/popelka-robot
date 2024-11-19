import _thread
import time

from pybricks.parameters import Port

from devices.SimpleMotor import SimpleMotor
from devices.SimpleUltraSonic import SimpleUltraSonic
from systems.LiftSystem import LiftSystem
from systems.LightSystem import LightSystem
from systems.GyroSystem import GyroSystem

class DriveSystem:
    def __init__(self, left_motor_port: Port, right_motor_port: Port, wheel_diameter_mm, axle_track_mm, base_speed,
                 correction_factor, light_system: LightSystem, lift_system: LiftSystem,
                 simple_ultra_sonic: SimpleUltraSonic, gyro_system: GyroSystem):
        # Initialize motors
        self.left_motor = SimpleMotor('left', left_motor_port)
        self.right_motor = SimpleMotor('right', right_motor_port)

        # Constants
        self.wheel_diameter_mm = wheel_diameter_mm
        self.axle_track_mm = axle_track_mm
        self.base_speed = base_speed
        self.correction_factor = correction_factor
        self.light_system = light_system
        self.lift_system = lift_system
        self.simple_ultra_sonic = simple_ultra_sonic
        self.gyro_system = gyro_system
        self.move_scale_factor = 1  # if distance doesn't quite match, adjust this
        self.rotate_scale_factor = 3.888  # Adjust this if needed

    def move_distance(self, distance_mm, use_correction=True):
        print("Starting move_distance of {} mm".format(distance_mm * self.move_scale_factor))

        # Reset motor angles
        self.left_motor.motor.reset_angle(0)
        self.right_motor.motor.reset_angle(0)

        wheel_circumference = 3.1416 * self.wheel_diameter_mm
        target_angle = (distance_mm * self.move_scale_factor / wheel_circumference) * 360.0  # degrees
        print("Target angle: {}".format(target_angle))

        # Start moving
        while True:
            # Get the average of the two motor angles
            left_angle = self.left_motor.motor.angle()
            right_angle = self.right_motor.motor.angle()
            average_angle = (left_angle + right_angle) / 2.0

            print("Left angle: {}, Right angle: {}, Average angle: {}, Target angle: {}".format(
                left_angle, right_angle, average_angle, target_angle))

            # Check if target distance is reached
            if distance_mm > 0:
                if average_angle >= target_angle:
                    # Target distance reached
                    print("Target angle reached.")
                    break
            else:
                if average_angle <= target_angle:
                    # Target distance reached
                    print("Target angle reached.")
                    break

            # Check if we are on the line
            if not self.light_system.is_on_line():
                # We are off the line, use gyro for correction
                angle = self.gyro_system.get_angle()
                print("Off the line. Gyro angle: {}".format(angle))
                # Calculate correction based on gyro angle
                # The correction factor may need to be adjusted based on testing
                correction = angle * self.correction_factor
                if angle > 0:
                    angle = min(angle, 10)
                else:
                    angle = max(angle, -10)
                correction = angle * self.correction_factor
            else:
                # We are on the line
                correction = 0
                # Reset gyro angle when back on line
                print("On the line..")
                
            if not use_correction:
                correction = 0

            # Adjust motor speeds based on correction
            left_speed = self.base_speed - correction
            right_speed = self.base_speed + correction

            # Ensure motor speeds are within allowed range
            max_speed = 1000  # Max motor speed (adjust as needed)
            left_speed = max(min(left_speed, max_speed), -max_speed)
            right_speed = max(min(right_speed, max_speed), -max_speed)

            # Set motor speeds
            if distance_mm > 0:
                self.left_motor.run(left_speed)
                self.right_motor.run(right_speed)
            else:
                self.left_motor.run(-left_speed)
                self.right_motor.run(-right_speed)

            # Debug statements
            print("Left speed: {}, Right speed: {}, Correction: {}".format(
                left_speed, right_speed, correction))

            # Check for ball detection
            if self.simple_ultra_sonic.is_object_in_front():
                # Handle ball detection logic
                time.sleep(0.35)
                print("Ball detected, initiating grab sequence.")
                _thread.start_new_thread(self.lift_system.grab_without_return, ())

            # Small delay to prevent tight loop
            time.sleep(0.01)  # wait 10 ms

        # Stop motors
        self.left_motor.stop()
        self.right_motor.stop()
        print("move_distance completed.")

    def rotate_angle(self, angle_degrees, speed=None):
        CORRECTION_VALUE = 3

        if speed is None:
            speed = self.base_speed + 100
        print("Starting rotate_angle of target {} degrees, real {} degrees".format(
            angle_degrees, angle_degrees * self.rotate_scale_factor))

        if angle_degrees < 0:
            angle_degrees += CORRECTION_VALUE   # Correct for overshoot
        else:
            angle_degrees -= CORRECTION_VALUE

        # Compute rotation distance
        rotation_circumference = 3.1416 * self.axle_track_mm
        rotation_distance_mm = (rotation_circumference * angle_degrees) / 360.0

        # Compute wheel rotation angle
        wheel_circumference = 3.1416 * self.wheel_diameter_mm
        wheel_rotation_angle = (rotation_distance_mm * self.rotate_scale_factor / wheel_circumference) * 360.0  # degrees

        # Use move_to_angle to move the motors
        self.left_motor.move_to_angle(wheel_rotation_angle, speed, wait=False)
        self.right_motor.move_to_angle(-wheel_rotation_angle, speed)

        # After rotation, reset gyro angle
        self.gyro_system.reset_angle()
        print("rotate_angle completed.")