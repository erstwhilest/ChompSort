import pygame
import random
from constants import *
import sortfunctions

class DataVisualizer:
	def __init__(self, data_count=1, rect=pygame.Rect(0,0,0,0), sound_manager=None):
		self.sound_manager = sound_manager
		self.rect = rect

		self.data_count = data_count
		self.data = []
		for i in range(data_count):
			self.data.append(i+1)

		self.data_rects = []
		self.data_colors = []

		self.positions = []
		data_width = rect.w/data_count
		data_height = rect.h/data_count
		for i in range(data_count):
			self.data_colors.append(WHITE)
			self.positions.append(i*data_width+rect.x)
			self.data_rects.append(pygame.Rect(self.positions[i], rect.h+rect.y-(self.data[i]*data_height), data_width-1, data_height*self.data[i]))
		
		self.sort_name=''
		self.generator=None
		self.sorting=False
	
	def set_sort(self, sort_name):
		self.sort_name=sort_name
		if sort_name == "Stooge Sort":
			self.generator=sortfunctions.stooge_sort(self.data,0,self.data_count-1)
		elif sort_name == "Cocktail Shaker Sort":
			self.generator=sortfunctions.cocktail_shaker_sort(self.data,self.data_count)
		elif sort_name == "Pancake Sort":
			self.generator=sortfunctions.pancake_sort(self.data)
	
	def clear_colors(self):
		for i in range(self.data_count):
			self.data_colors[i] = WHITE

	def step(self):
		if self.sorting:
			try:
				self.clear_colors()
				l,h=next(self.generator)
				self.data_colors[l]=GREEN
				self.data_colors[h]=GREEN
				# self.data_colors[l:h]=GREEN
			except StopIteration:
				self.sorting=False
			

	def render(self, screen):
		for i in range(self.data_count):
			self.data_rects[i].x=self.positions[self.data[i]-1]
			pygame.draw.rect(screen, self.data_colors[i], self.data_rects[i])

	def shuffle_data(self):
		random.shuffle(self.data)