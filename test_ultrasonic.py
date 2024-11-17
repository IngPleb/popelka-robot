#!/usr/bin/env pybricks-micropython


from pybricks.parameters import Port

from devices.SimpleUltraSonic import SimpleUltraSonic

from pybricks.tools import wait

ultra_sonic_sensor = SimpleUltraSonic(Port.S1, 100)

while True:
    print(ultra_sonic_sensor.is_object_in_front())
    wait(200)    
