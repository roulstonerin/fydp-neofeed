#!/usr/bin/env python


# Import required libraries

from flask import Flask, render_template_string, request   # Importing the Flask modules
from time import sleep      # Import sleep module from time library 
import sys
import time
import RPi.GPIO as GPIO
'''
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Set all pins as output

print("Setting up pins")
GPIO.setup(18,GPIO.OUT) # step control pin = 18
GPIO.output(18, False) 
GPIO.setup(22,GPIO.OUT) # direction control pin = 22
GPIO.output(22, False)'''
    
def initialize_motor():
  
    # Use BCM GPIO references instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Define GPIO signals to use
    # Set all pins as output
    print("Setting up pins")
    GPIO.setup(18,GPIO.OUT) # step control pin = 18
    GPIO.output(18, False) 
    GPIO.setup(22,GPIO.OUT) # direction control pin = 22
    GPIO.output(22, False)

def cleanup_motor():
    GPIO.output( 18, GPIO.LOW )
    GPIO.output( 22, GPIO.LOW )
    GPIO.cleanup()

def change_motor_height(height,moves_up):
    # Initialise variables
    WaitTime = 0.05 # changed to 500ms
    stepCounter = 0
    stepsToRotate = height*1000*(1/0.3) # convert meters to steps (1 step = 0.3mm)
    
            
    print("Steps to rotate received:",int(stepsToRotate))
    
    try:
        if moves_up:
            GPIO.output( 22, GPIO.HIGH) # high is clockwise and low is counterclockwise
        else:
            GPIO.output(22,GPIO.LOW)
        for stepCounter in range(int(stepsToRotate)):
            #for pin in range(0, 4):
            GPIO.output(18, GPIO.HIGH)
            time.sleep(WaitTime/2)
            GPIO.output(18, GPIO.LOW)
            time.sleep(WaitTime/2)
    
    except KeyboardInterrupt:
        cleanup_motor()
        exit(1)
    
    GPIO.output( 18, False )
    GPIO.output( 22, False )
    #cleanup_motor()

        