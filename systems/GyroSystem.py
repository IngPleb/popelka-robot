class GyroSystem:
    def __init__(self, gyro):
        self.gyro = gyro

    def getAngle(self):
        return self.gyro.getAngle()

    def reset(self):
        self.gyro.reset()
