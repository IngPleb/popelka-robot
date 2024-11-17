#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

from pybricks.tools import wait


def main():
    lift_motor = Motor(Port.D)
    
    while True:
        lift_motor.run(400)
        print(lift_motor.angle())


if __name__ == "__main__":
    main()
