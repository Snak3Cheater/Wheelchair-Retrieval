# Initialization -------------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
# from tkinter import *
# from ObjectRecognition import TFLite_detection_webcamv2 as Tflite
# import sys
import cv2
import random
import UltrasonicSensor
# Left Motors ---------------------------
LMotor_1 = 16
LMotor_2 = 15
sleeptime = 1
# Right Motors --------------------------
RMotor_1 = 11
RMotor_2 = 13
# Ultrasonic sensors -------------------
FrontTRIG = 37  # 36
FrontECHO = 36  # 37
# GPIO Setup --------------------
#GPIO.setup(FrontTRIG, GPIO.OUT)
#GPIO.setup(FrontECHO, GPIO.IN)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(servo_R, GPIO.OUT)
#GPIO.setup(servo_L, GPIO.OUT)



def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LMotor_1, GPIO.OUT)
    GPIO.setup(LMotor_2, GPIO.OUT)
    GPIO.setup(RMotor_1, GPIO.OUT)
    GPIO.setup(RMotor_2, GPIO.OUT)
    # Ultrasonic Sensor
    GPIO.setup(FrontTRIG, GPIO.OUT)
    GPIO.setup(FrontECHO, GPIO.IN)
    

def stop(sleep_T):
    init()
    print('stopping')
    GPIO.output(LMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.LOW)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)
    GPIO.cleanup()

def forward(sleep_T):
    init()
    print('Going Forward')
    GPIO.output(LMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.HIGH)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)
    GPIO.cleanup()


def turn_L(sleep_T):
    init()
    print('Turning Left')
    GPIO.output(LMotor_2, GPIO.HIGH)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.HIGH)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)
    GPIO.cleanup()


def reverse(sleep_T):
    init()
    print('Reversing')
    GPIO.output(LMotor_2, GPIO.HIGH)
    GPIO.output(LMotor_1, GPIO.LOW)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(RMotor_1, GPIO.HIGH)
    time.sleep(sleep_T)
    GPIO.cleanup()


def turn_R(sleep_T):
    init()
    print('Turning Right')
    GPIO.output(LMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)
    GPIO.cleanup()


def pivot_L(sleep_T):
    init()
    print('Pivoting Left')
    GPIO.output(LMotor_2, GPIO.HIGH)
    GPIO.output(LMotor_1, GPIO.LOW)
    GPIO.output(RMotor_2, GPIO.HIGH)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)
    GPIO.cleanup()


def pivot_R(sleep_T):
    init()
    print('Pivoting Right')
    GPIO.output(LMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(RMotor_1, GPIO.HIGH)
    time.sleep(sleep_T)
    GPIO.cleanup()


def front_check():
    init()
    dist = UltrasonicSensor.front_sensing()
    time.sleep(1.5)

    if dist < 50:
        print('Too close:', dist)
        init()
        pivot_L(1)
        reverse(1)
        #dist = UltrasonicSensor.front_sensing()
        #time.sleep(1)
    if dist < 30:
        print('Still too close:', dist)
        init()
        reverse(5)
        init()
        pivot_L(2)
        #dist = UltrasonicSensor.front_sensing()
        #time.sleep(1)


def auto_drive():

    x = random.randrange(0, 3)
    if x == 0:
        front_check()
        init()
        forward(1)
        #if x == 1:
        #    front_check()
        #    init()
        #    pivot_L(0.5)
    if x == 2:
        front_check()
        init()
        turn_R(0.5)
    if x == 3:
        front_check()
        init()
        turn_L(0.5)
        
