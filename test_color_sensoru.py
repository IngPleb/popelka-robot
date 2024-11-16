#!/usr/bin/env pybricks-micropython
import time

from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor
while True:
    color_sensor = ColorSensor(Port.S1)
    print(color_sensor.rgb())
    time.sleep(0.01)
    

    #modrá kulička má b přes 50