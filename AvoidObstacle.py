#!/usr/bin/python

from Rover import Rover
import random
import time


rover = Rover()

try:
    while True:
        rover.forward()

        while not rover.forward_sensor_triggered():
            time.sleep(0.1)

        if random.choice([True, False]):
            rover.turn_left()
        else:
            rover.turn_right()

        while rover.forward_sensor_triggered():
            time.sleep(0.2)

        time.sleep(0.5)


except KeyboardInterrupt:
    pass

rover.stop()
rover.cleanup()

