import pygame
import random
from constants import *
import sortfunctions

class DataVisualizer:
	def __init__(self, data_count=1, rect=pygame.Rect(0,0,0,0), sound_manager=None):
		self.sound_manager = sound_manager
		self.rect = rect

		self.data_count = data_count
		self.data = [i+1 for i in range(data_count)]

		self.data_rects = []
		self.data_colors = []

		self.positions = []
		self.data_width = rect.w/data_count
		self.data_height = rect.h/data_count
		for i in range(data_count):
			self.data_colors.append(WHITE)
			self.positions.append(i*self.data_width+rect.x)
			self.data_rects.append(pygame.Rect(
				self.positions[i],
				rect.h+rect.y-(self.data[i]*self.data_height),
				self.data_width-1,
				self.data_height*self.data[i]))
		
		self.sort_name=''
		self.generator=None
		self.sorting=False
	
	def resize(self, size):
		self.data_count = size
		self.positions.clear()
		self.data_colors.clear()
		self.data_rects.clear()
		self.data = [i+1 for i in range(self.data_count)]
		self.data_width = self.rect.w/self.data_count
		self.data_height = self.rect.h/self.data_count
		for i in range(self.data_count):
			self.data_colors.append(WHITE)
			self.positions.append(i*self.data_width+self.rect.x)
			self.data_rects.append(pygame.Rect(
				self.positions[i],
				self.rect.h+self.rect.y-(self.data[i]*self.data_height),
				self.data_width-1,
				self.data_height*self.data[i]))
		self.sorting = False
		self.restart_sort()
	
	def restart_sort(self):
		if self.sort_name == "Stooge Sort":
			self.generator=sortfunctions.stooge_sort(self.data,0,self.data_count-1)
		elif self.sort_name == "Cycle Sort":
			self.generator=sortfunctions.cycle_sort(self.data)
		elif self.sort_name == "Cocktail Shaker Sort":
			self.generator = sortfunctions.cocktail_shaker_sort(self.data)
		elif self.sort_name == "Pancake Sort":
			self.generator = sortfunctions.pancake_sort(self.data)
	
	def set_sort(self, sort_name):
		self.sort_name=sort_name
		if sort_name == "Stooge Sort":
			self.generator=sortfunctions.stooge_sort(self.data,0,self.data_count-1)
		elif sort_name == "Cycle Sort":
			self.generator=sortfunctions.cycle_sort(self.data)
		elif sort_name == "Cocktail Shaker Sort":
			self.generator=sortfunctions.cocktail_shaker_sort(self.data)
		elif sort_name == "Pancake Sort":
			self.generator=sortfunctions.pancake_sort(self.data)
	
	def clear_colors(self):
		for i in range(self.data_count):
			self.data_colors[i] = WHITE

	def step(self):
		if self.sorting:
			try:
				self.clear_colors()
				p1,p2=next(self.generator)
				self.data_colors[p1]=GREEN
				self.data_colors[p2]=GREEN
				self.sound_manager.play(self.data[p1]/self.data_count)
			except StopIteration:
				self.sorting=False
			

	def render(self, screen):
		for i in range(self.data_count):
			# self.data_rects[i].x=self.positions[self.data[i]-1]
			self.data_rects[i].y=SCREEN_RES[1]-(self.data[i])*self.data_height
			self.data_rects[i].h=(self.data[i])*self.data_height
			pygame.draw.rect(screen, self.data_colors[i], self.data_rects[i])

	def shuffle_data(self):
		random.shuffle(self.data)
