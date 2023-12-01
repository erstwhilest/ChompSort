import pygame
# import numpy as np
# from scipy import signal

class SoundManager:
	def __init__(self):
		triangle=[]
		self.frequency_count = 50
		for i in range(self.frequency_count):
			triangle.append(pygame.mixer.Sound('sounds/triangle'+str(i)+'.wav'))

	def select_sound(self, name):
		if name == "sine":
			self.select_sound = self.sine
		elif name == "triangle":
			self.select_sound = self.triangle
		else:
			self.select_sound = self.triangle


	def play(self, val):
		self.selected_sound[int(val*self.frequency_count)].play()