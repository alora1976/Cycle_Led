import RPi.GPIO as GPIO       ## Import GPIO library
    
GPIO.cleanup()

BLUE_LED = 8
RED_LED = 16
GREEN_LED = 18
BUTTON = 22

GPIO.setmode(GPIO.BOARD)      ## Use board pin numbering
GPIO.setup(BLUE_LED, GPIO.OUT)      ## Setup GPIO Pin 8 to OUT
GPIO.setup(RED_LED,GPIO.OUT)
GPIO.setup(GREEN_LED,GPIO.OUT)
GPIO.setup(BUTTON,GPIO.IN)

timer = 0
stop = 0



while stop == 0:
    if timer % 30000 == 0:
        GPIO.output(BLUE_LED,True)
        GPIO.output(RED_LED,False)
        GPIO.output(GREEN_LED,False)
    elif timer % 30000 == 10000:
        GPIO.output(BLUE_LED,False)
        GPIO.output(RED_LED,True)
        GPIO.output(GREEN_LED,False)
    elif timer % 30000 == 20000:
        GPIO.output(BLUE_LED,False)
        GPIO.output(RED_LED,False)
        GPIO.output(GREEN_LED,True)
    timer = timer + 1
    if GPIO.input(22) == 1:
        stop = 1
