import RPi.GPIO as GPIO
import time

# app needs to receive location data of pillbox so the pilltaking can be
# configured based on the patients whereabouts

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

output_pin1 = 18
output_pin2 = 23
output_pin2 = 24
output_pin2 = 25

input_pin1 = 7
input_pin2 = 12
input_pin2 = 12
input_pin2 = 12

# intialiser set
GPIO.setup(output_pin1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(25, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(input_pin1, GPIO.IN)
GPIO.setup(input_pin2, GPIO.IN)

print(time.strftime('%d-%m-%Y %H:%M:%S'))

reset = True
blue_led = True
circuit_broken = False
current_t = time.strftime('%S')

while(True):
        # restart program to reset LEDs
        if reset is True:
                GPIO.output(output_pin1, GPIO.LOW)
                GPIO.output(output_pin2, GPIO.LOW)
                reset = False
                print("LEDs RESET!")
                time.sleep(1)
        
        # print every second
        if time.strftime('%S') != current_t:
		current_t = time.strftime('%S')
		print(current_t)

        # between 0 - 30 seconds; blueLED
        if int(time.strftime('%S')) <= 30:
                if blue_led is True:
                        GPIO.output(output_pin1, GPIO.HIGH)
                        GPIO.output(output_pin2, GPIO.LOW)
                        blue_led = False
                        
                # pill timer reset
                if (int(time.strftime('%S')) % 10) == 0:
                        circuit_broken = False
                        GPIO.output(output_pin1, GPIO.HIGH)

                # bluLED circuit broken
                if GPIO.input(input_pin1) == 0:
                        circuit_broken = True
                        GPIO.output(output_pin1, GPIO.LOW)
                        
                else:
                        circuit_broken = False
                        GPIO.output(output_pin1, GPIO.HIGH)
                        
                # time.sleep(1)

        # between 31 - 60 seconds; redLED // NIGHT
        else:
                if blue_led is False:
                        GPIO.output(output_pin1, GPIO.LOW)
                        GPIO.output(output_pin2, GPIO.HIGH)
                        blue_led = True
                        
                # pill timer reset
                if (int(time.strftime('%S')) % 10) == 0:
                        circuit_broken = False
                        GPIO.output(output_pin2, GPIO.HIGH)

                # redLED circuit broken
                if GPIO.input(input_pin2) == 0:
                        circuit_broken = True
                        GPIO.output(output_pin2, GPIO.LOW)
                        
                else:
                        circuit_broken = False
                        GPIO.output(output_pin2, GPIO.HIGH)

                # time.sleep(1)
