import pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(200)

class SoundManager:
	def __init__(self):
		self.triangle=[]
		self.sine=[]
		self.selected_sound = self.triangle
		self.frequency_count = 50
		for i in range(self.frequency_count):
			self.triangle.append(pygame.mixer.Sound('sounds/triangle'+str(i+1)+'.wav'))
			self.sine.append(pygame.mixer.Sound('sounds/sine'+str(i+1)+'.wav'))

	def select_sound(self, name):
		if name == "Sine":
			self.selected_sound = self.sine
		elif name == "Triangle":
			self.selected_sound = self.triangle
		else:
			self.selected_sound = self.triangle


	def play(self, val):
		pygame.mixer.find_channel().play(self.selected_sound[int(val*self.frequency_count)-1])