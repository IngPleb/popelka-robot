class Waypoint:
    def __init__(self, x, y, use_correction=True):
        self.x = x
        self.y = y
        self.use_correction = use_correction
        self.flags = {}
