#!/usr/bin/env pybricks-micropython

import os
import sys
import time

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port

while True:
    color_sensor = ColorSensor(Port.S1)
    print(color_sensor.rgb())
    time.sleep(0.01)
