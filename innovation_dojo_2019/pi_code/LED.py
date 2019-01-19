import RPi.GPIO as GPIO
import time

# app needs to receive location data of pillbox so the pilltaking can be
# configured based on the patients whereabouts

input1 = 12
output1 = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(output1, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(input1, GPIO.IN)

print(time.strftime('%d-%m-%Y %H:%M:%S'))

circuit_broken = False

current_t = time.strftime('%S')

while True:
	if time.strftime('%S') != current_t:
		current_t = time.strftime('%S')
		#print(current_t)
		#print"INPUT:", GPIO.input(24)

	if (int(time.strftime('%S')) % 20) == 0:
		circuit_broken = False
		GPIO.output(output1, GPIO.HIGH)		

	if GPIO.input(input1) == 0:
		circuit_broken = True
		GPIO.output(output1, GPIO.LOW)

	else:
		circuit_broken = False
		GPIO.output(output1, GPIO.HIGH)
