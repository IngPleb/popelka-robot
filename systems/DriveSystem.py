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

    def move_distance(self, distance_mm, use_correction=True):
        # Reset motor angles
        self.left_motor.motor.reset_angle(0)
        self.right_motor.motor.reset_angle(0)

        wheel_circumference = 3.1416 * self.wheel_diameter_mm
        target_angle = (distance_mm*self.move_scale_factor / wheel_circumference) * 360.0  # degrees

        # Start moving
        while True:
            # Get the average of the two motor angles
            left_angle = self.left_motor.motor.angle()
            right_angle = self.right_motor.motor.angle()
            average_angle = (left_angle + right_angle) / 2.0

            if distance_mm > 0:
                if average_angle >= target_angle:
                    # Target distance reached
                    break

            if distance_mm < 0:
                if average_angle <= target_angle:
                    # Target distance reached
                    break

            # Set motor speeds
            if distance_mm > 0:
                self.left_motor.run(self.base_speed)
                self.right_motor.run(self.base_speed)
            if distance_mm < 0:
                self.left_motor.run(-self.base_speed)
                self.right_motor.run(-self.base_speed)

            # Check for ball detection
            #if self.simple_ultra_sonic.is_object_in_front():
             #   time.sleep(0.55)
              #  _thread.start_new_thread(self.lift_system.grab_without_return, ())

            # Small delay to prevent tight loop
            time.sleep(0.01)  # wait 10 ms

        # Stop motors
        self.left_motor.stop()
        self.right_motor.stop()

    def rotate_angle(self, angle_degrees, speed=None, use_correction=True):
        CORRECTION_VALUE = 3
        
        if speed is None:
            speed = self.base_speed + 100
        
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
