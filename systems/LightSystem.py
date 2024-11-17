import random

from pybricks.ev3devices import ColorSensor


def is_ball(r, g, b):
    if r > 20: return True
    if g > 50: return True
    if b > 60: return True
    return False


class LightSystem:
    def __init__(self, sensor_port, blue_threshold_on_line, dead_zone=3, initial_correction_magnitude=1,
                 max_correction_magnitude=3, readings_to_consider=2):
        self.color_sensor = ColorSensor(sensor_port)
        self.BLUE_THRESHOLD_ON_LINE = blue_threshold_on_line
        self.DEAD_ZONE = dead_zone
        self.correction_direction = random.choice([-1, 1])  # Random initial direction
        self.correction_magnitude = initial_correction_magnitude
        self.max_correction_magnitude = max_correction_magnitude
        self.readings_to_consider = readings_to_consider
        self.deviation_history = []
        self.same_or_worse_counter = 0
        self.successful_readings = 0
        self.just_went_off_line = True  # Flag to check if we just went off the line

    def get_correction(self):
        r, g, b = self.color_sensor.rgb()
        print("RGB values:", r, g, b)

        if is_ball(r, g, b):
            print("Ball detected, returning 0")
            return 0

        blue_value = b
        print("Blue value:", blue_value)

        # Calculate deviation from the threshold
        deviation = abs(blue_value - self.BLUE_THRESHOLD_ON_LINE)
        print("Deviation:", deviation)

        # Check if we are within the dead zone
        if deviation <= self.DEAD_ZONE:
            print("Within dead zone, resetting correction values")
            # We're on the line
            self.correction_magnitude = 1  # Reset magnitude
            self.same_or_worse_counter = 0
            self.deviation_history = []
            self.successful_readings += 1
            self.just_went_off_line = True  # Reset flag
            return 0  # No correction needed
        else:
            print("Outside dead zone, updating correction values")
            # Off the line
            self.successful_readings = 0  # Reset successful readings counter

            # If we just went off the line, reverse correction direction
            if self.just_went_off_line:
                self.correction_direction *= -1  # Reverse direction
                self.just_went_off_line = False
                print("Just went off line, reversing direction:", self.correction_direction)

            # Append current deviation to history
            self.deviation_history.append(deviation)
            if len(self.deviation_history) > self.readings_to_consider:
                self.deviation_history.pop(0)

            print("Deviation history:", self.deviation_history)

            # Check if deviation is improving
            if len(self.deviation_history) >= 2:
                if self.deviation_history[-1] >= self.deviation_history[-2]:
                    # Deviation is same or worse
                    self.same_or_worse_counter += 1
                    print("Deviation is same or worse, counter:", self.same_or_worse_counter)
                else:
                    # Deviation is improving
                    self.same_or_worse_counter = 0  # Reset counter
                    print("Deviation is improving, counter reset")

            if self.same_or_worse_counter >= self.readings_to_consider:
                # Reverse correction direction and increase magnitude
                self.correction_direction *= -1
                self.correction_magnitude = min(self.correction_magnitude + 1, self.max_correction_magnitude)
                self.same_or_worse_counter = 0  # Reset counter
                self.deviation_history = []  # Reset deviation history
                print("Reversing direction and increasing magnitude, direction:", self.correction_direction,
                      "magnitude:", self.correction_magnitude)

            # Compute correction
            correction = self.correction_direction * self.correction_magnitude
            print("Correction:", correction)

            return correction

    def is_ball_detected(self):
        r, g, b = self.color_sensor.rgb()
        print("Checking for ball, RGB values:", r, g, b)
        return is_ball(r, g, b)
