# Popelka Robot - ČVUT Robosoutěž 2024

A robot implementation for ČVUT Robosoutěž 2024, representing the Benešovsko region. The project achieved 8 points in the competition.

## Overview

This project contains the code for an EV3 LEGO Mindstorms robot designed to collect and deposit balls into a collector. The implementation uses the "Look Who's Back" (LWB) strategy with hardcoded paths due to sensor reliability issues.

## Project Structure

- `devices` - Base device implementations
  - `devices/SimpleMotor.py` - Motor control wrapper
  - `devices/SimpleUltraSonic.py` - Ultrasonic sensor wrapper

- `systems` - Higher-level system implementations
  - `systems/DriveSystem.py` - Robot movement control
  - `systems/GyroSystem.py` - Gyroscope handling
  - `systems/LiftSystem.py` - Ball collection mechanism
  - `systems/LightSystem.py` - Line following system
  - `systems/System.py` - Base system class

## Key Features

- Hardcoded movement paths for reliable operation
- Motor control system with precise angle movements
- Ball collection mechanism using lift system
- Basic movement primitives (rotate, move forward/backward)

## Dependencies

- pybricks v3.5.0
- EV3 LEGO Mindstorms hardware

## Team Achievement

Best performing team from the Benešovsko region in ČVUT Robosoutěž 2024.

## Technical Notes

- Uses `pybricks-micropython` for EV3 control
- Movement calculations based on wheel diameter (68.8mm) and axle track (92.5mm)
- Base movement speed of 400 units with correction factor of 29