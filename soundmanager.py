import pygame
# import numpy as np
# from scipy import signal

class SoundManager:
	def __init__(self):
		# containers for final sounds
		# self.triangle = []
		# self.sine = []

		# self.selected_sound = self.triangle

		# pygame.mixer.init()
		# sample_rate = 44100
		# base_freq = 440
		
		# self.frequency_count = 50

		# for i in range(self.frequency_count+1):
		# 	# create raw wave
		# 	sine_sound = (4096*np.sin((i/10)*2.0*np.pi*base_freq*np.arange(0,sample_rate)/sample_rate)).astype(np.int16) # sine wave
		# 	triangle_sound = (4096*signal.sawtooth((i/self.frequency_count*3)*2*np.pi*base_freq*np.arange(0,sample_rate)/sample_rate,.5)).astype(np.int16) # triangle wave

		# 	# smoothing
		# 	maxtime=70/1000 # in ms
		# 	low=100
		# 	fade=1500

		# 	r=(0,low)
		# 	sine_sound[r[0]:r[1]]=0
		# 	triangle_sound[r[0]:r[1]]=0

		# 	r=(low,fade)
		# 	sine_sound[r[0]:r[1]]=sine_sound[r[0]:r[1]]*np.arange(r[1]-r[0])/(r[1]-r[0])
		# 	triangle_sound[r[0]:r[1]]=triangle_sound[r[0]:r[1]]*np.arange(r[1]-r[0])/(r[1]-r[0])

		# 	r=(int(sample_rate*(maxtime)-fade),int(sample_rate*(maxtime)-low))
		# 	sine_sound[r[0]:r[1]]=sine_sound[r[0]:r[1]]*np.arange(r[1]-r[0],0,-1)/(r[1]-r[0])
		# 	triangle_sound[r[0]:r[1]]=triangle_sound[r[0]:r[1]]*np.arange(r[1]-r[0],0,-1)/(r[1]-r[0])

		# 	r=(int(sample_rate*(maxtime)-low),0)
		# 	sine_sound[r[0]::]=0
		# 	triangle_sound[r[0]::]=0

		# 	# duplicate channel
		# 	sine_final=np.c_[sine_sound,sine_sound]
		# 	triangle_final=np.c_[triangle_sound,triangle_sound]
		# 	self.sine.append(pygame.sndarray.make_sound(sine_final))
		# 	self.triangle.append(pygame.sndarray.make_sound(triangle_final))
		# sine=[]
		triangle=[]
		self.frequency_count = 50
		for i in range(self.frequency_count):
			# sine.append(pygame.mixer.Sound('sounds/sine'+str(i)+'.wav'))
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