from pybricks.ev3devices import ColorSensor


def is_ball(r, g, b):
    if r + g + b > 100:
        return True


class LightSystem:
    def __init__(self, sensor_port, blue_threshold_on_line, dead_zone=1, initial_correction_magnitude=1,
                 max_correction_magnitude=3, readings_to_consider=2):
        self.color_sensor = ColorSensor(sensor_port)
        self.BLUE_THRESHOLD_ON_LINE = blue_threshold_on_line
        self.DEAD_ZONE = dead_zone
        self.correction_direction = 1  # Start with default direction
        self.correction_magnitude = initial_correction_magnitude
        self.max_correction_magnitude = max_correction_magnitude
        self.readings_to_consider = readings_to_consider  # Number of readings to consider for trend
        self.deviation_history = []
        self.same_or_worse_counter = 0
        self.successful_readings = 0

    def get_correction(self):
        r, g, b = self.color_sensor.rgb()

        if is_ball(r, g, b):
            # Ball detected => we can't rely on the sensor
            return 0

        blue_value = b

        # Calculate deviation from the threshold
        deviation = abs(blue_value - self.BLUE_THRESHOLD_ON_LINE)

        # Check if we are within the dead zone
        if deviation <= self.DEAD_ZONE:
            # We're on the line
            self.correction_direction = 1  # Reset to default
            self.correction_magnitude = 1  # Reset magnitude
            self.same_or_worse_counter = 0
            self.deviation_history = []
            self.successful_readings += 1
            return 0  # No correction needed
        else:
            # Off the line
            self.successful_readings = 0  # Reset successful readings counter

            # Append current deviation to history
            self.deviation_history.append(deviation)
            if len(self.deviation_history) > self.readings_to_consider:
                self.deviation_history.pop(0)

            # Check if deviation is improving
            if len(self.deviation_history) >= 2:
                if self.deviation_history[-1] >= self.deviation_history[-2]:
                    # Deviation is same or worse
                    self.same_or_worse_counter += 1
                else:
                    # Deviation is improving
                    self.same_or_worse_counter = 0  # Reset counter

            if self.same_or_worse_counter >= self.readings_to_consider:
                # Reverse correction direction and increase magnitude
                self.correction_direction *= -1
                self.correction_magnitude = min(self.correction_magnitude + 1, self.max_correction_magnitude)
                self.same_or_worse_counter = 0  # Reset counter
                self.deviation_history = []  # Reset deviation history

            # Compute correction
            correction = self.correction_direction * self.correction_magnitude

            return correction

    def is_ball_detected(self):
        r, g, b = self.color_sensor.rgb()
        return is_ball(r, g, b)
