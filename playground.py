#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import ColorSensor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the EV3 Brick.

ev3 = EV3Brick()

# Initialize the peripherals
color_sensor_port = Port.S1


def main():
    color_sensor = ColorSensor(color_sensor_port)

    while True:
        print(color_sensor.reflection())
        wait(250)


if __name__ == "__main__":
    main()
