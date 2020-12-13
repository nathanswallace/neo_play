#main entry for the programs 

import time
import board
import random
import RPi.GPIO as GPIO
import neopixel #https://circuitpython.readthedocs.io/projects/neopixel/en/latest/api.html   

GPIO.setup(11, GPIO.IN)

class Led_Strip:
	def __init__(self, size):
		self.neo_leds=neopixel.NeoPixel(board.D18, size, auto_write=False)
		#self.leds=neopixel.NeoPixel(board.D18, size)
		self.led_values=[]
		self.size=size
		for i in range(self.size):
			self.led_values.append((0,0,0))
		
	def clear_led_values(self):
		for i in range(self.size):
			self.led_values[i]=(0,0,0)
		
	#led=[ind, r, g, b]
	def update_led(self, led):
		self.led_values[led[0]]=[led[1],led[2],led[3]]
		
	def run(self):
		for i in range(self.size):
			self.neo_leds[i]=self.led_values[i]
			
		self.neo_leds.show()
		

# Duration of one cycle in seconds 
#CycleTime = .0250
CycleTime = 0.03


# Main method that starts the program 
if __name__ == "__main__":
	program_running = True
	
	door_open = False 
		
	led_strip=Led_Strip(150)
	#clears it out, on init all values are 0,0,0
	led_strip.run()
	
	while program_running:
		cycle_start_time=time.time()
		
		#when magnet is not close to sensor it returns 1, True
		#when magnet is close to sensor it returns 0, False
		door_open=GPIO.input(11)
		
		if door_open:
			#print("door open")
			led=random.randint(0,149)
			led_strip.update_led([led,25,0,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,25,0,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,25,0,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,25,0,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,25,0,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,25,0,0])
		
		
			led_strip.run()

		else:
			#print("door closed")
			led=random.randint(0,149)
			led_strip.update_led([led,0,25,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,0,25,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,0,25,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,0,25,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,0,25,0])
			
			led=random.randint(0,149)
			led_strip.update_led([led,0,25,0])
		
			led_strip.run()
		
		#sleep until ready to cycle again
		sleeptime = CycleTime-(time.time()-cycle_start_time)
		if sleeptime > 0:
			time.sleep(sleeptime)

			
		led_strip.clear_led_values()
		led_strip.run()
			
	
	
			

