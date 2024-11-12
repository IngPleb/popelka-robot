#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor
from pybricks.hubs import EV3Brick
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the EV3 Brick.

ev3 = EV3Brick()


celkem_vzdalensost = 8000 # celkem vzdálenost kterou to má ujet
koeficient_vzdalenosti = 160 #bylo by to moc velký, ale mohla by to klidně být jedn
korekce_vzdalenosti_dole = 7 #procenta navíc dole z vdálenosti
rychlost_zvedani = 1000 
rychlost_klesani = 650


# Motors
motor_B = Motor(Port.B)

motor_B.reset_angle(0)

motor_B.run_time(rychlost_klesani, celkem_vzdalensost*(1+0.01*korekce_vzdalenosti_dole)*koeficient_vzdalenosti/rychlost_klesani) 


motor_B.run_time(-rychlost_zvedani, celkem_vzdalensost*koeficient_vzdalenosti/rychlost_zvedani)