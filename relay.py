import time

import RPi.GPIO as GPIO

def change_relay(duration):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(15, GPIO.OUT)
	GPIO.output(15, GPIO.HIGH)
	time.sleep(duration)
	GPIO.output(15, GPIO.LOW)
	GPIO.cleanup()

change_relay(5)
