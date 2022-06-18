#! /usr/bin/python3
"""
Author: Sri
Purpose: To encapsulate functionality of a Motor
Background: 
   - The Speed and Direction of spinning for each motor is controlled 
     by varying the PWM signal (speed) and two GPIO pins (direction)
"""

import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setwarnings(False)

class Motor:

    def __init__ (self, pinEnable, pinFwd, pinBwd, pwmFreq=20, maxSpeed=100,minSpeed=40):
        """ set the Motor up to a default state"""

        self._pwmFreq   = pwmFreq
        self._maxSpeed  = maxSpeed
        self._minSpeed  = minSpeed
        self._pinEnable = pinEnable
        self._pinFwd    = pinFwd
        self._pinBwd    = pinBwd
        
        # set all three pins as output pins
        gp.setup ([self._pinEnable, self._pinFwd, self._pinBwd],gp.OUT)
        self._pwmHandle = gp.PWM (pinEnable, pwmFreq)
        self._speed = 0

    
    def deets(self):
        """ provide details of Motor"""
        deet = 'Current speed : {} PWMFreq: {} Max: {} Min: {} E: {} F: {} B: {}'
        return deet.format(self._speed, self._pwmFreq,self._maxSpeed,self._minSpeed,self._pinEnable,self._pinFwd,self._pinBwd)
    
    def get_speed(self):
        return self._speed
    
    def set_speed(self, speed):
        # clip speed to limits

        if speed == 0 : 
            self._speed = 0
            return

        self._speed = min(speed, self._maxSpeed) if speed > 0 else max(speed, -self._maxSpeed)

        if (abs(self._speed) < self._minSpeed):
            if (self._speed < 0):
                self._speed = -self._minSpeed
            else:
                self._speed = self._minSpeed
        
    
    def move(self):
        if self._speed == 0 : # stop
            self._pwmHandle.stop()
            gp.output ([self._pinEnable, self._pinFwd, self._pinBwd], gp.LOW)

        elif self._speed < 0: # move backward
            self._pwmHandle.start(-self._speed)
            gp.output (self._pinFwd, gp.LOW)
            gp.output (self._pinBwd, gp.HIGH)

        else:  # move forward
            self._pwmHandle.start(self._speed)
            gp.output (self._pinFwd, gp.HIGH)
            gp.output (self._pinBwd, gp.LOW)
            
