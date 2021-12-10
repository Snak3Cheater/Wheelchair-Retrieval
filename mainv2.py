# Initialization -------------------------------------------------------------------------
import RPi.GPIO as GPIO
import time
from tkinter import *
import TFLite_detection_webcam as Tflite
import TFLite_detection_hand as Tflite2
# import sys
import random
from UltrasonicSensor import front_sensing
import auto_drive as auto

# Left Motors ---------------------------
LMotor_1 = 16
LMotor_2 = 15
sleeptime = 1
# Right Motors --------------------------
RMotor_1 = 11
RMotor_2 = 13
# Clamping Servo Motors -----------------
servo_R = 33
servo_L = 32
# Ultrasonic sensors -------------------
FrontTRIG = 37 #36
FrontECHO = 36 #37
# GPIO Setup --------------------
GPIO.setup(FrontTRIG, GPIO.OUT)
GPIO.setup(FrontECHO, GPIO.IN)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_R, GPIO.OUT)
GPIO.setup(servo_L, GPIO.OUT)
pwm = GPIO.PWM(servo_R, 50)
pwm2 = GPIO.PWM(servo_L, 50)
# --------------------------------------
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(LMotor_1, GPIO.OUT)
# GPIO.setup(LMotor_2, GPIO.OUT)
# GPIO.setup(RMotor_1, GPIO.OUT)
# GPIO.setup(RMotor_2, GPIO.OUT)
# ---------------------------------------
sleep_T = 0.100
GPIO.cleanup()


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LMotor_1, GPIO.OUT)
    GPIO.setup(LMotor_2, GPIO.OUT)
    GPIO.setup(RMotor_1, GPIO.OUT)
    GPIO.setup(RMotor_2, GPIO.OUT)
    # Ultrasonic Sensor
    GPIO.setup(FrontTRIG, GPIO.OUT)
    GPIO.setup(FrontECHO, GPIO.IN)
    

def init_servo():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servo_R, GPIO.OUT)
    GPIO.setup(servo_L, GPIO.OUT)
    pwm.start(0)
    pwm2.start(0)


# Clamp Controls --------------------------------------
def clamp(event):
    init_servo()
    print("Clamping")
    button_z.config(bg="red")
    pwm.ChangeDutyCycle(5)  # clockwise rotation
    time.sleep(1.1*sleep_T)
    pwm.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(10)  # counter rotation
    time.sleep(sleep_T)
    pwm2.ChangeDutyCycle(0)


def retract(event):
    init_servo()
    print("Retracting")
    button_x.config(bg="red")
    pwm.ChangeDutyCycle(10)  # counter rotation
    time.sleep(sleep_T)
    pwm.ChangeDutyCycle(0)
    pwm2.ChangeDutyCycle(5)  # clockwise rotation
    time.sleep(1.1*sleep_T)
    pwm2.ChangeDutyCycle(0)


# DC Motor Controls ---------------------------------------
def forward(event):
    init()
    # print("Going Forward")
    button_w.config(bg="red")
    GPIO.output(LMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.HIGH)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)
    # distance = front_sensing()
    # print(distance)
    # if distance <= 40.00:
    #     print("READY TO LATCH")
    

def turn_L(event):
    init()
    # print('Turning Left')
    button_a.config(bg="red")
    GPIO.output(LMotor_2, GPIO.HIGH)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.HIGH)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)


def reverse(event):
    init()
    # print("Reversing")
    button_s.config(bg="red")
    GPIO.output(LMotor_2, GPIO.HIGH)
    GPIO.output(LMotor_1, GPIO.LOW)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(RMotor_1, GPIO.HIGH)
    time.sleep(sleep_T)


def turn_R(event):
    init()
    # print('Turning Right')
    button_d.config(bg="red")
    GPIO.output(LMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)


def key_release(event):
    button_w.config(bg='white')
    button_a.config(bg='white')
    button_s.config(bg='white')
    button_d.config(bg='white')
    # Clamp Buttons
    button_z.config(bg='white')
    button_x.config(bg='white')
    GPIO.cleanup()


def close(event):
    GPIO.cleanup
    window.destroy()


def manual_mode():
    if button_manual['relief'] == RAISED:
        button_manual.config(relief=SUNKEN, bg="Orange")
        print("Manual: ON")
        window.bind("<w>", forward)
        window.bind("<KeyRelease-w>", key_release)
        window.bind("<a>", turn_L)
        window.bind("<KeyRelease-a>", key_release)
        window.bind("<s>", reverse)
        window.bind("<KeyRelease-s>", key_release)
        window.bind("<d>", turn_R)
        window.bind("<KeyRelease-d>", key_release)
        # Clamp Controls
        window.bind("<z>", clamp)
        window.bind("<KeyRelease-z>", key_release)
        window.bind("<x>", retract)
        window.bind("<KeyRelease-x>", key_release)
    else:
        button_manual['relief'] = RAISED
        button_manual.config(relief=RAISED, bg="White")
        print("Manual: OFF")
        window.unbind("<w>")
        window.unbind("<KeyRelease-w>")
        window.unbind("<a>")
        window.unbind("<KeyRelease-a>")
        window.unbind("<s>")
        window.unbind("<KeyRelease-s>")
        window.unbind("<d>")
        window.unbind("<KeyRelease-d>")
        # Clamp Controls
        window.unbind("<z>")
        window.unbind("<KeyRelease-z>")
        window.unbind("<x>")
        window.unbind("<KeyRelease-x>")


def explore():
    timeout = time.time() + 10*4
    while True:
        auto.auto_drive()
        if time.time() > timeout:
            break

# WASD Simulated Feedback GUI --------------------------------------------------------
window = Tk()
window.title("Keyboard GUI")
window.geometry("600x600")

frame = Frame(window)
frame.pack()

button_w = Button(frame, text="W", height=4, width=9, font=35, bg="white")
button_w.grid(row=0, column=1)
button_a = Button(frame, text="A", height=4, width=9, font=35, bg="white")
button_a.grid(row=1, column=0)
button_s = Button(frame, text="S", height=4, width=9, font=35, bg="white")
button_s.grid(row=1, column=1)
button_d = Button(frame, text="D", height=4, width=9, font=35, bg="white")
button_d.grid(row=1, column=2)
# Clamping Feedback GUI ---------------------------------------------------
button_z = Button(frame, text="Z", height=4, width=9, font=35, bg="white")
button_z.grid(row=2, column=0)
button_x = Button(frame, text="X", height=4, width=9, font=35, bg="white")
button_x.grid(row=2, column=1)
# Feature Buttons --------------------------------------------------------
button_manual = Button(frame, text="MANUAL MODE", height=4, width=14, font=35, bg="white", command=manual_mode)
button_manual.grid(row=0, column=6)
button_WheelchairSearch = Button(frame, text="SEARCH MODE", height=4, width=14, font=35, bg="white", command=Tflite.object_recognition)
button_WheelchairSearch.grid(row=1, column=6)
button_PersonSearch = Button(frame, text="SEARCH PERSON", height=4, width=14, font=35, bg="white", command=Tflite2.object_recognition)
button_PersonSearch.grid(row=2, column=6)
button_Explore = Button(frame, text="EXPLORE MODE", height=4, width=14, font=35, bg="white", command=explore)
button_Explore.grid(row=3, column=6)

# QUIT PROGRAM ------------------------------------------
window.bind("<q>", close)

window.mainloop()

