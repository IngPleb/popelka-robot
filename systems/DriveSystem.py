import _thread
import time

from pybricks.parameters import Port

from devices.SimpleMotor import SimpleMotor
from devices.SimpleUltraSonic import SimpleUltraSonic
from systems.LiftSystem import LiftSystem
from systems.LightSystem import LightSystem


class DriveSystem:
    def __init__(self, left_motor_port: Port, right_motor_port: Port, wheel_diameter_mm, axle_track_mm, base_speed,
                 correction_factor, light_system: LightSystem, lift_system: LiftSystem,
                 simple_ultra_sonic: SimpleUltraSonic):
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
        self.move_scale_factor = 1  # if distance dont quite match, adjust this
        self.rotate_scale_factor = 3.888 #and this

    def move_distance(self, distance_mm, general_correction_rule):
        print("Starting move_distance of " + str(distance_mm*self.move_scale_factor) + " mm with correction" + str(general_correction_rule))
        temp_correction_rule = general_correction_rule

        # Reset motor angles
        self.left_motor.motor.reset_angle(0)
        self.right_motor.motor.reset_angle(0)

        wheel_circumference = 3.1416 * self.wheel_diameter_mm
        target_angle = (distance_mm*self.move_scale_factor / wheel_circumference) * 360.0  # degrees
        print("Target angle: " + str(target_angle))

        # Start moving
        while True:
            # Get the average of the two motor angles
            left_angle = self.left_motor.motor.angle()
            right_angle = self.right_motor.motor.angle()
            average_angle = (left_angle + right_angle) / 2.0

            print("Left angle: " + str(left_angle) + ", Right angle: " + str(right_angle) + ", Average angle: " + str(
                average_angle) + "Target angle: " + str(target_angle))

            if distance_mm > 0:
                if average_angle >= target_angle:
                    # Target distance reached
                    print("Target angle reached.")
                    break

            if distance_mm < 0:
                if average_angle <= target_angle:
                    # Target distance reached
                    print("Target angle reached.")
                    break

            if temp_correction_rule is True:
                print("correction is running")
                # Get correction from LightSystem
                correction = self.light_system.get_correction()
                # Adjust motor speeds
                left_speed = self.base_speed - (correction * self.correction_factor)
                right_speed = self.base_speed + (correction * self.correction_factor)

            else:
                left_speed = self.base_speed
                right_speed = self.base_speed

            # Set motor speeds
            if distance_mm > 0:
                self.left_motor.run(left_speed)
                self.right_motor.run(right_speed)
            if distance_mm < 0:
                self.left_motor.run(-left_speed)
                self.right_motor.run(-right_speed)

            # Debug statements
            print("Left angle: " + str(left_angle) + ", Right angle: " + str(right_angle) + ", Correction: " + str(
                general_correction_rule))
            print("Left speed: " + str(left_speed) + ", Right speed: " + str(right_speed))

            # Check for ball detection
            if self.simple_ultra_sonic.is_object_in_front():
                if general_correction_rule is True:
                    temp_correction_rule = False
                time.sleep(0.35)
                print("Ball detected, initiating grab sequence.")
                _thread.start_new_thread(self.lift_system.grab_without_return, ())
                temp_correction_rule = True

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
        print("Starting rotate_angle of target" + str(angle_degrees) + " degrees, real" + str(angle_degrees*self.rotate_scale_factor) +"degrees")
        
        if angle_degrees < 0:
            angle_degrees = angle_degrees + CORRECTION_VALUE   # Correct for overshoot
        else:
            angle_degrees = angle_degrees - CORRECTION_VALUE

        # Compute rotation distance
        rotation_circumference = 3.1416 * self.axle_track_mm
        rotation_distance_mm = (rotation_circumference * angle_degrees) / 360.0

        # Compute wheel rotation angle
        wheel_circumference = 3.1416 * self.wheel_diameter_mm
        wheel_rotation_angle = (rotation_distance_mm*self.rotate_scale_factor / wheel_circumference) * 360.0  # degrees

        # Use move_to_angle to move the motors
        self.left_motor.move_to_angle(wheel_rotation_angle, speed, wait=False)
        self.right_motor.move_to_angle(-wheel_rotation_angle, speed)

        print("rotate_angle completed.")
