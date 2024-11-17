#!/usr/bin/env pybricks-micropython

import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pybricks.parameters import Port
from systems.LiftSystem import LiftSystem

lift_port = Port.D


def main():
    lift = LiftSystem(lift_port)

    lift.run_continuously()

    while True:
        pass


if __name__ == "__main__":
    main()
