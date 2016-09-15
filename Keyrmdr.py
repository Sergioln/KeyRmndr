
import time # For sleep function
import pygame # For play music
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superus$

# Module level constants
LED1 = 11
PIN_DOOR = 12

# Setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PIN_DOOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Check the state of the door
def door():
    # Block until HIGH to LOW level detected
    if GPIO.input(PIN_DOOR):
        GPIO.wait_for_edge(PIN_DOOR, GPIO.FALLING)
    print ("Puerta abierta")
    GPIO.output(LED1, GPIO.HIGH)
    pygame.mixer.init(frequency=16000)
    pygame.mixer.music.load("keys.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    pygame.mixer.quit()
    # Block until LOW to HIGH level detected
    if not GPIO.input(PIN_DOOR):
        GPIO.wait_for_edge(PIN_DOOR, GPIO.RISING)
    print ("Puerta cerrada")
    GPIO.output(LED1, GPIO.LOW)
    #pygame.mixer.music.stop()

