#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.tools import wait

from systems.LightSystem import LightSystem


def main():
    system = LightSystem(Port.S1, blue_threshold_on_line=7)

    while True:
        print(system.is_on_line())
        wait(200)


if __name__ == "__main__":
    main()
