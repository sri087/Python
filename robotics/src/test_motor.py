#! /usr/bin/env python3
"""
Author: Sri
Purpose: to test the Motor class
"""

import time
from Motor import Motor

leftWheel  = Motor(16,20,21,maxSpeed=80,minSpeed=40)         #,2000,80)
rightWheel = Motor(13,19,26,maxSpeed=80,minSpeed=40)         #,2000,80)

delay = 2
defaultSpeed = 60

template = 'PWMFreq: {} Max: {} Min: {} E: {} F: {} B: {}'
#----------------------------------------------------------
def test_deets():
    """test if properly initialized"""

    assert leftWheel.deets() == template.format(2000,80,40,16,20,21)
    assert rightWheel.deets() == template.format(2000,80,40,13,19,26)

#----------------------------------------------------------
def test_speed():
    """test if speed is set properly"""

    leftWheel.set_speed(0)
    rightWheel.set_speed(0)
    assert leftWheel.get_speed() == 0
    assert rightWheel.get_speed() == 0

    leftWheel.set_speed(-120)
    rightWheel.set_speed(30)
    assert leftWheel.get_speed() == -80
    assert rightWheel.get_speed() == 40

    leftWheel.set_speed(-40)
    rightWheel.set_speed(60)
    assert leftWheel.get_speed() == -40
    assert rightWheel.get_speed() == 60

    leftWheel.set_speed(-40)
    rightWheel.set_speed(90)
    assert leftWheel.get_speed() == -40
    assert rightWheel.get_speed() == 80

    leftWheel.set_speed(-39)
    rightWheel.set_speed(-42)
    assert leftWheel.get_speed() == -40
    assert rightWheel.get_speed() == -42

#----------------------------------------------------------
def move():
    """
    This function will move the robot, so the test has 
    to be verified visually
    """

    forward()
    backward()

    spin_right()
    spin_left()

    turn_right_forward()
    turn_right_backward()

    turn_left_forward()
    turn_left_backward()

    test_stop()

#----------------------------------------------------------
def forward():
    print('forward')
    leftWheel.set_speed(40)
    rightWheel.set_speed(40)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def backward():
    print('backward')
    leftWheel.set_speed(-40)
    rightWheel.set_speed(-40)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def spin_right():
    print('spin right')
    leftWheel.set_speed(40)
    rightWheel.set_speed(-40)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def spin_left():
    print('spin left')
    leftWheel.set_speed(-40)
    rightWheel.set_speed(40)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def turn_right_forward():
    print('right forward')
    leftWheel.set_speed(60)
    rightWheel.set_speed(40)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def turn_left_forward():
    print('left forward')
    leftWheel.set_speed(40)
    rightWheel.set_speed(60)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def turn_left_backward():
    print('left backward')
    leftWheel.set_speed(-40)
    rightWheel.set_speed(-60)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def turn_right_backward():
    print('right backward')
    leftWheel.set_speed(-60)
    rightWheel.set_speed(-40)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def test_stop():
    print('stop')
    leftWheel.set_speed(0)
    rightWheel.set_speed(0)

    leftWheel.move()
    rightWheel.move()
    time.sleep(delay)

#----------------------------------------------------------
def main():
    #test_deets()
    test_speed()
    move()

if __name__=='__main__':
    main()

