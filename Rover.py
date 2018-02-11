#!/usr/bin/python

import PiMotor
import time
import RPi.GPIO as GPIO


class Rover:

    def __init__(self):
        self._motor_front_left =  PiMotor.Motor("MOTOR1", 2)
        self._motor_back_left =  PiMotor.Motor("MOTOR2", 2)
        self._motor_back_right =  PiMotor.Motor("MOTOR3", 2)
        self._motor_front_right =  PiMotor.Motor("MOTOR4", 2)
        self._forward_sensor = PiMotor.Sensor("ULTRASONIC", 50)
        self._speed = 100

        self._motor_all = PiMotor.LinkedMotors(
            self._motor_front_left,
            self._motor_front_right,
            self._motor_back_left,
            self._motor_back_right,
        )

        self._motor_left = PiMotor.LinkedMotors(
            self._motor_front_left,
            self._motor_back_left,
        )

        self._motor_right = PiMotor.LinkedMotors(
            self._motor_front_right,
            self._motor_back_right,
        )

        self._arrow_left = PiMotor.Arrow(1)
        self._arrow_forward = PiMotor.Arrow(2)
        self._arrow_right = PiMotor.Arrow(3) 
        self._arrow_back = PiMotor.Arrow(4)

    def _test_motor(self, motor):
        motor.forward(self._speed)
        time.sleep(5)
        motor.reverse(self._speed)
        time.sleep(5)
        motor.stop()

    def test_motor_front_left(self):
        self._test_motor(self._motor_front_left)
        
    def test_motor_front_right(self):
        self._test_motor(self._motor_front_right)
        
    def test_motor_back_left(self):
        self._test_motor(self._motor_back_left)
        
    def test_motor_back_right(self):
        self._test_motor(self._motor_back_right)
        
    def forward(self):
        self.stop()
        self._arrow_forward.on()
        self._motor_all.forward(self._speed)

    def reverse(self):
        self.stop()
        self._arrow_back.on()
        self._motor_all.reverse(self._speed)

    def turn_left(self):
        self.stop()
        self._arrow_left.on()
        self._motor_left.reverse(self._speed)
        self._motor_right.forward(self._speed)

    def turn_right(self):
        self.stop()
        self._arrow_right.on()
        self._motor_left.forward(self._speed)
        self._motor_right.reverse(self._speed)

    def stop(self):
        self._arrow_forward.off()
        self._arrow_back.off()
        self._arrow_left.off()
        self._arrow_right.off()
        self._motor_all.stop()

    def forward_sensor_triggered(self):
        self._forward_sensor.trigger()
        return self._forward_sensor.Triggered

    def cleanup(self):
        GPIO.cleanup()
