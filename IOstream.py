import board
import RPi.GPIO as GPIO
from gpiozero import InputDevice
import neopixel
import Adafruit_DHT as dht
from time import sleep
import socket

# function for getting num string from VM
def string_exchange(sent_message):
	sock.send(sent_message)
	return sock.recv(4096)
	
# function for displaying speed limit
def print_speed(speed):
	pixels = neopixel.NeoPixel(board.D18, 75)
	
	for x in range(0,70):   # initializing display
		pixels[x] = (0,0,0)
		
	if int(speed / 10) == 1:   # printing first digit of speed limit
		for x in range(21,30):
			pixels[x] = (255,255,255)
	elif int(speed / 10) == 2:
		for x in range(0,10):
			pixels[x] = (255,255,255)
		for x in range(15,26):
			pixels[x] = (255,255,255)
		for x in range(30,35):
			pixels[x] = (255,255,255)
	elif int(speed / 10) == 3:
		for x in range(0,6):
			pixels[x] = (255,255,255)
		for x in range(15,35):
			pixels[x] = (255,255,255)
	elif int(speed / 10) == 4:
		for x in range(10,15):
			pixels[x] = (255,255,255)
		for x in range(21,35):
			pixels[x] = (255,255,255)
	elif int(speed / 10) == 5:
		for x in range(0,6):
			pixels[x] = (255,255,255)
		for x in range(10,21):
			pixels[x] = (255,255,255)
		for x in range(26,35):
			pixels[x] = (255,255,255)
	elif int(speed / 10) == 6:
		for x in range(0,21):
			pixels[x] = (255,255,255)
		for x in range(26,35):
			pixels[x] = (255,255,255)
			
	if speed % 10 == 0 and int(speed / 10) != 0:   # printing second digit of speed limit
		for x in range(35,65):
			pixels[x] = (255,255,255)
	elif speed % 10 == 5:
		for x in range(35,41):
			pixels[x] = (255,255,255)
		for x in range(45,56):
			pixels[x] = (255,255,255)
		for x in range (60,70):
			pixels[x] = (255,255,255)
			
	if speed == 69:
		for x in range(0,21):
			pixels[x] = (255,20,203)
		for x in range(26,35):
			pixels[x] = (255,20,203)
		for x in range(35,56):
			pixels[x] = (255,20,203)
		for x in range(60,70):
			pixels[x] = (255,20,203)
			
# function for traffic redirection (stepper motor)
def redirect(direction):
	# Direction pin from controller
	DIR = 10
	# Step pin from controller
	STEP = 8
	# 0/1 used to signify clockwise or counterclockwise.
	CW = 1
	CCW = 0

	# Setup pin layout on PI
	GPIO.setmode(GPIO.BOARD)

	# Establish Pins in software
	GPIO.setup(DIR, GPIO.OUT)
	GPIO.setup(STEP, GPIO.OUT)

	# Set the first direction you want it to spin
	GPIO.output(DIR, CW)
	
	if direction == 1:   # only rotates sign if necessary
		for x in range(400):   # adjust rotation amount by stepper

			# Set one coil winding to high
			GPIO.output(STEP,GPIO.HIGH)
			# Allow it to get there.
			sleep(.005) # Dictates how fast stepper motor will run
			# Set coil winding to low
			GPIO.output(STEP,GPIO.LOW)
			sleep(.005) # Dictates how fast stepper motor will run

# function for reading sensors
def ht():
	DHT = 4
	humid, temp = dht.read_retry(dht.DHT22, DHT)
	if temp == 50:
		sleep(3)
		humid, temp = dht.read_retry(dht.DHT22, DHT)
	return humid, temp
	
def rain():
	no_rain = InputDevice(25)
	
	if not no_rain.is_active:
		return 1
	else:
		return 0

def soil_moisture():
	no_moist = InputDevice(21)
	
	if not no_moist.is_active:
		return 1
	else:
		return 0

# function for streaming camera (might need to separate)
		
def main():
	# initialize socket connection with VM
	#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#sock.connect(('172.98.142.220', 8080))
	
	print_speed(35)
	
	# while True:
		# # sampling sensors
		# humidity, temp = ht()
		# rain_status = rain()
		# soil_status = soil_moisture()
		# sent_message = str(humidity) + ':' + str(temp) + ':' + str(rain_status) + ':' + str(soil_status)
		# print(sent_message)
	
		# # send data to VM and receive sign parameters
		# sign_param = string_exchange(sent_message).split(':')
	
		# # execute sign parameters
		# speed = sign_param(0)
		# print_speed(speed)
		
		# direction = sign_param(1)
		# redirect(direction)
		
		# road_cond = sign_param(2)
	
if __name__ == "__main__":
	main()
