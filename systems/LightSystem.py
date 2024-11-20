from pybricks.ev3devices import ColorSensor





class LightSystem:
    def __init__(self, sensor_port, blue_threshold_on_line):
        self.color_sensor = ColorSensor(sensor_port)
        self.BLUE_THRESHOLD_ON_LINE = blue_threshold_on_line

    def is_ball(self):
        r, g, b = self.color_sensor.rgb()
        sum = r + g + b
        if sum > 30 or b>14:
            print("ball detected by light system")
            return True

        # Add more

        return False

    def is_on_line(self):
        # Get the blue value from the sensor
        r,g,b = self.color_sensor.rgb()
        blue_value = b
        
        if self.is_ball():
            return True
        # Determine if we are on the line based on the blue threshold
        return blue_value <= self.BLUE_THRESHOLD_ON_LINE
    
    
