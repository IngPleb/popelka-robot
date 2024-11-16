from pybricks.ev3devices import ColorSensor

class LightCorrectionSystem:
    def __init__(self, sensor_port, blue_threshold_on_line, blue_threshold_off_line, history_length=5):
        self.color_sensor = ColorSensor(sensor_port)
        self.BLUE_THRESHOLD_ON_LINE = blue_threshold_on_line
        self.BLUE_THRESHOLD_OFF_LINE = blue_threshold_off_line
        self.history = []  # To store recent corrections
        self.history_length = history_length
        print("LightCorrectionSystem initialized with sensor_port:", sensor_port)

    def get_correction(self):
        # Get RGB values
        _, _, b = self.color_sensor.rgb()
        print("Current blue value:", b)

        # Determine the line state
        if b <= self.BLUE_THRESHOLD_ON_LINE:
            correction = -1  # Correction to stay on the line
            print("Correction set to -1 (on the line)")
        elif b >= self.BLUE_THRESHOLD_OFF_LINE:
            correction = 1  # Correction to return to the line
            print("Correction set to 1 (off the line)")
        else:
            correction = 0  # No correction needed
            print("Correction set to 0 (no correction needed)")

        # Update history
        self.update_history(correction)

        # Adjust correction magnitude based on history
        adjusted_correction = self.adjust_correction(correction, b)
        print("Adjusted correction:", adjusted_correction)

        return adjusted_correction

    def update_history(self, correction):
        # Add the latest correction to history
        self.history.append(correction)
        print("Updated history:", self.history)
        # Trim history to maintain a fixed length
        if len(self.history) > self.history_length:
            self.history.pop(0)
            print("Trimmed history to maintain length:", self.history)

    def adjust_correction(self, correction, blue_value):
        # If the robot is back on the line, reset history
        if blue_value <= self.BLUE_THRESHOLD_ON_LINE:
            self.history.clear()
            print("History cleared as robot is back on the line")
            return correction

        # If the robot remains off the line, increase correction magnitude
        if len(self.history) > 1 and all(c != 0 for c in self.history):
            magnitude = sum(self.history) / len(self.history)  # Average of recent corrections
            print("Average magnitude of recent corrections:", magnitude)
            return correction * (1 + abs(magnitude))  # Scale correction dynamically

        return correction