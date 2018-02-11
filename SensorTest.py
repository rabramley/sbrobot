#!/usr/bin/python

from Rover import Rover


rover = Rover()

try:
    while True:
        if rover.forward_sensor_triggered():
            print('Trigger')
        else:
            print('Not') 


except KeyboardInterrupt:
    pass

rover.stop()
rover.cleanup()

