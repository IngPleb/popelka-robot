from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


class CorrectionAction:
    MOVE_LEFT = 1
    MOVE_RIGHT = 2
    NONE = 0

class LightCorrectionSystem:
    def __init__(self, sensor_port: Port, reference_value: int = 15, tolerance: int = 15):
        self.sensor = ColorSensor(sensor_port)
        self.reference_value = reference_value
        self.tolerance = tolerance
        self.last_action = CorrectionAction.NONE
        self.last_error = 0
        self.consecutive_same_direction = 0
        
    def process_input(self) -> tuple[int, int]:
        """
        Process sensor input and determine correction action.
        Returns (action, magnitude)
        """
        current_value = self.sensor.reflection()
        error = current_value - self.reference_value
        
        # Within tolerance - no correction needed
        if abs(error) <= self.tolerance:
            self.reset_correction_history()
            return CorrectionAction.NONE, 0
            
        # Determine direction based on error
        action = CorrectionAction.MOVE_LEFT if error > 0 else CorrectionAction.MOVE_RIGHT
        
        # Check if correction direction changed
        if action != self.last_action:
            self.consecutive_same_direction = 0
        else:
            self.consecutive_same_direction += 1
        
        # Adjust magnitude based on error and history
        base_magnitude = min(abs(error), 100)  # Cap at 100
        
        # If same direction multiple times, increase correction
        if self.consecutive_same_direction > 2:
            base_magnitude *= 1.5
        
        # If error is getting worse, increase correction
        if abs(error) > abs(self.last_error):
            base_magnitude *= 1.2
            
        self.last_action = action
        self.last_error = error
        
        return action, int(base_magnitude)
    
    def reset_correction_history(self):
        """Reset correction history when back on track"""
        self.last_action = CorrectionAction.NONE
        self.last_error = 0
        self.consecutive_same_direction = 0