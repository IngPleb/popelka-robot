#!/usr/bin/env pybricks-micropython

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
