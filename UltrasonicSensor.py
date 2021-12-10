# Ultrasonic Initialization
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

# Pin Assignments ------------------------------------------------------------------------
FrontTRIG = 37 #36
FrontECHO = 36 #37
# RearTRIG = 17
# RearECHO = 27
#GPIO.setup(FrontTRIG, GPIO.OUT)
#GPIO.setup(FrontECHO, GPIO.IN)
# GPIO.setup(RearTRIG, GPIO.OUT)
# GPIO.setup(RearECHO, GPIO.IN)

def front_sensing():
    # print('Distance Measurement In Progress')
    #GPIO.output(FrontTRIG, False)
    # print('Waiting For Sensor To Settle')
    # time.sleep(1)

    # The HC-SR04 sensor requires a short 10uS pulse to trigger
    # the module, which will cause the sensor to start the ranging
    # program (8 ultrasound bursts at 40 kHz) in order to obtain an echo response.
    # So, to create our trigger pulse, we set out trigger pin high for 10uS then set it low again.

    GPIO.output(FrontTRIG, True)
    time.sleep(0.00001)
    GPIO.output(FrontTRIG, False)

    while GPIO.input(FrontECHO) == 0:
        fpulse_start = time.time()

    while GPIO.input(FrontECHO) == 1:
        fpulse_end = time.time()

    fpulse_duration = fpulse_end - fpulse_start
    fdistance = round(fpulse_duration * 17150, 2)  # Distance in centimeters
    fdistance = round(fdistance, 2)  # Distance in centimeters
    # fdistance = fdistance*.01  # Distance in meters
    # print(fdistance)
    return fdistance  # Returning the front distance value from sensor
