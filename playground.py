#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.tools import wait

from devices.SimpleUltraSonic import SimpleUltraSonic
from systems.LiftSystem import LiftSystem


def main():
    simple_ultrasonic = SimpleUltraSonic(Port.S2, 120)
    lift_system = LiftSystem(Port.D)
    while True:
        print(simple_ultrasonic.is_object_in_front())
        print(simple_ultrasonic)
        if simple_ultrasonic.is_object_in_front():
            lift_system.grab_without_return()
        wait(200)


if __name__ == "__main__":
    main()
