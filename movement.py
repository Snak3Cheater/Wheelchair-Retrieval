import RPi.GPIO as GPIO
import time
from tkinter import *
# import sys
# import random
# from sensor import distance

# Left Motors ---------------------------
LMotor_1 = 16
LMotor_2 = 15
sleeptime = 1
# Right Motors --------------------------
RMotor_1 = 11
RMotor_2 = 13
# --------------------------------------
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(LMotor_1, GPIO.OUT)
# GPIO.setup(LMotor_2, GPIO.OUT)
# GPIO.setup(RMotor_1, GPIO.OUT)
# GPIO.setup(RMotor_2, GPIO.OUT)
# ---------------------------------------
sleep_T = 0.050
GPIO.cleanup()


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LMotor_1, GPIO.OUT)
    GPIO.setup(LMotor_2, GPIO.OUT)
    GPIO.setup(RMotor_1, GPIO.OUT)
    GPIO.setup(RMotor_2, GPIO.OUT)
    

def forward(event):
    init()
    print("Going Forward")
    button_w.config(bg="red")
    GPIO.output(LMotor_2, GPIO.LOW)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.HIGH)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)


def turn_L(event):
    init()
    print('Turning Left')
    button_a.config(bg="red")
    GPIO.output(LMotor_2, GPIO.HIGH)
    GPIO.output(LMotor_1, GPIO.HIGH)
    GPIO.output(RMotor_2, GPIO.HIGH)
    GPIO.output(RMotor_1, GPIO.LOW)
    time.sleep(sleep_T)


def reverse(event):
    init()
    print("Reversing")
    button_s.config(bg="red")
    GPIO.output(LMotor_2, GPIO.HIGH)
    GPIO.output(LMotor_1, GPIO.LOW)
    GPIO.output(RMotor_2, GPIO.LOW)
    GPIO.output(RMotor_1, GPIO.HIGH)
    time.sleep(sleep_T)


def turn_R(event):
    init()
    print('Turning Right')
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
    GPIO.cleanup()


def close(event):
    GPIO.cleanup()
    window.destroy()


# def pivot_L(tf):
#     gpio.output(7, True)
#     gpio.output(11, False)
#     gpio.output(13, True)
#     gpio.output(15, False)
#     time.sleep(tf)
#     gpio.cleanup()
#
# def pivot_R(tf):
#     gpio.output(7, False)
#     gpio.output(11, True)
#     gpio.output(13, False)
#     gpio.output(15, True)
#     time.sleep(tf)
#     gpio.cleanup()


# def key_in(event):
#     initial()
#     print('Key:', event.char)
#     key_press = event.char
#     sleep_T = 0.050
#
#     if key_press.lower() == 'w':
#         forward(sleep_T)
#     elif key_press.lower() == 's':
#         reverse(sleep_T)
#     elif key_press.lower() == 'a':
#         turn_L(sleep_T)
#     elif key_press.lower() == 'd':
#         turn_R(sleep_T)
#     elif key_press.lower() == 'q':
#         pivot_L(sleep_T)
#     elif key_press.lower() == 'e':
#         pivot_R(sleep_T)
#     else:
#         gpio.cleanup()

    # currentDistance = distance('cm')
    # print('Current Distance is:', currentDistance)

    # if currentDistance < 30:
    #     initial()
    #     reverse(2)

# WASD Simulated Feedback GUI--------------------------------------------------------
window = Tk()
window.title("Keyboard GUI")
window.geometry("600x300")

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

# WASD COMMANDS ---------------------------------------------------
window.bind("<w>", forward)
window.bind("<KeyRelease-w>", key_release)
window.bind("<a>", turn_L)
window.bind("<KeyRelease-a>", key_release)
window.bind("<s>", reverse)
window.bind("<KeyRelease-s>", key_release)
window.bind("<d>", turn_R)
window.bind("<KeyRelease-d>", key_release)

# QUIT PROGRAM ------------------------------------------
window.bind("<q>", close)

window.mainloop()


# For the autonomous driving, remove for manual movement above
'''
def front_check():
    initial()
    dist = distance()

    if dist < 15:
        print ('Too close:', dist)
        initial()
        reverse(2)
        dist = distance()
        if dist < 15:
            print ('Still too close:', dist)
            initial()
            pivot_L(3)
            initial()
            reverse(2)
            dist = distance()
            if dist < 15:
                print ('Still too close, manually move:', dist)
                sys.exit()
def auto_drive():
    tf = 0.050
    x = random.randrange(0,4)

    if x == 0:
        for y in range(30):
            front_check()
            initial()
            forward(tf)
    if x == 1:
        for y in range(30):
            front_check()
            initial()
            pivot_L(tf)
    if x == 2:
        for y in range(30):
            front_check()
            initial()
            turn_R(tf)
    if x == 3:
        for y in range(30):
            front_check()
            initial()
            turn_L(tf)
for z in range(10):
    auto_drive()
'''
