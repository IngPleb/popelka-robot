#!/usr/bin/env pybricks-micropython


from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

while True:
    color_sensor = ColorSensor(Port.S1)
    print(color_sensor.rgb())
    wait(200)
