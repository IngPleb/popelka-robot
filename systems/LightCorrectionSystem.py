class LightCorrectionSystem:
    def __init__(self, sensor_port, blue_threshold_on_line, blue_threshold_off_line, history_length=5):
        from pybricks.ev3devices import ColorSensor
        self.color_sensor = ColorSensor(sensor_port)
        self.BLUE_THRESHOLD_ON_LINE = blue_threshold_on_line
        self.BLUE_THRESHOLD_OFF_LINE = blue_threshold_off_line
        self.history = []
        self.history_length = history_length
        self.DEAD_ZONE = 1
        self.MIN_CORRECTION_THRESHOLD = 0.2

    def get_correction(self):
        r, g, b = self.color_sensor.rgb()

        # Dead zone logic
        if self.BLUE_THRESHOLD_ON_LINE - self.DEAD_ZONE <= b <= self.BLUE_THRESHOLD_ON_LINE + self.DEAD_ZONE:
            return 0  # No correction needed
        elif b > self.BLUE_THRESHOLD_ON_LINE + self.DEAD_ZONE:
            return 1  # Off the line (right)
        elif b < self.BLUE_THRESHOLD_ON_LINE - self.DEAD_ZONE:
            return -1  # Off the line (left)

    def get_smoothed_correction(self, current_correction):
        self.history.append(current_correction)
        if len(self.history) > self.history_length:
            self.history.pop(0)
        return sum(self.history) / len(self.history)

    def adjust_correction(self, correction, blue_value):
        deviation = abs(blue_value - self.BLUE_THRESHOLD_ON_LINE)
        if deviation < self.MIN_CORRECTION_THRESHOLD:
            return 0  # Ignore minor deviations
        scaled_correction = correction * (1 + deviation / 10)  # Scale correction dynamically
        return scaled_correction
