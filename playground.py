#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait


def main():
    gyro = GyroSensor(Port.S4)
    gyro.reset_angle(0)
    while True:
        print(gyro.angle())
        wait(200)


if __name__ == "__main__":
    main()
