import RPi.GPIO as GPIO
import time

# app needs to receive location data of pillbox so the pilltaking can be
# configured based on the patients whereabouts

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

n = 25

print("LED should be ON")
GPIO.setup(n, GPIO.OUT, initial = GPIO.HIGH)



time.sleep(2)

print("LED should be OFF")
GPIO.output(n, GPIO.LOW)

time.sleep(2)

print("LED should be ON")
GPIO.output(n, GPIO.HIGH)

print("LED should now flash 3 times")
GPIO.output(n, GPIO.LOW)
time.sleep(0.3)

#1
GPIO.output(n, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(n, GPIO.LOW)
time.sleep(0.3)

#2
GPIO.output(n, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(n, GPIO.LOW)
time.sleep(0.3)

#3
GPIO.output(n, GPIO.HIGH)
time.sleep(0.3)
GPIO.output(n, GPIO.LOW)

print("Program exited")
