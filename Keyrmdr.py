
import time # For sleep function
import pygame # For play music
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superus$

# Module constants
LED1 = 11
DOOR_SWITCH = 12

# Setup pins
GPIO.setmode(GPIO.BOARD) #Use the board naming pins
GPIO.setup(LED1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(DOOR_SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Set the pullup resist 

# Check the state of the door
def door():
    # Block until HIGH to LOW level detected, first check if the door is opened
    if GPIO.input(DOOR_SWITCH):
        GPIO.wait_for_edge(DOOR_SWITCH, GPIO.FALLING)
    print ("Puerta abierta")
    #switch on the led
    GPIO.output(LED1, GPIO.HIGH)
    #Play the reminder "Juana coge las llaves"
    pygame.mixer.init(frequency=16000)
    pygame.mixer.music.load("keys.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.quit()
    
    # Block until LOW to HIGH level detected, first check if the door is closed
    if not GPIO.input(DOOR_SWITCH):
        GPIO.wait_for_edge(DOOR_SWITCH, GPIO.RISING)
    print ("Puerta cerrada")
    #switch off the LED
    GPIO.output(LED1, GPIO.LOW)

