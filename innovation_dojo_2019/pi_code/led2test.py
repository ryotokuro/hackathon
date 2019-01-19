import RPi.GPIO as GPIO
import time

# app needs to receive location data of pillbox so the pilltaking can be
# configured based on the patients whereabouts

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(18, GPIO.IN)

print(time.strftime('%d-%m-%Y %H:%M:%S'))

circuit_broken = False

current_t = time.strftime('%S')

while True:
	if time.strftime('%S') != current_t:
		current_t = time.strftime('%S')
		#print(current_t)
		#print"INPUT:", GPIO.input(24)

        # every 20 seconds, reset and LED on
	if (int(time.strftime('%S')) % 20) == 0:
		circuit_broken = False
		GPIO.output(23, GPIO.HIGH)

	if GPIO.input(18) == 0:
		circuit_broken = True
		GPIO.output(23, GPIO.LOW)

	else:
		circuit_broken = False
		GPIO.output(23, GPIO.HIGH)

print("23 OFF, 25 ON")
                        print "bluLED:", GPIO.input(7)
                        print "redLED:", GPIO.input(12)
                        time.sleep(2)
                        
        elif (int(time.strftime('%S')) % 5) == 0 and twentyThree == False:
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(25, GPIO.LOW)
                twentyThree = True
                print("23 ON, 25 OFF")
                print "bluLED:", GPIO.input(7)
                print "redLED:", GPIO.input(12)
                time.sleep(2)
