import pygame
from PIL import Image
from random import shuffle
import sortfunctions

class PixelArray:
	def __init__(self, filename, location):
		image = Image.open(filename)
		self.pixel_map=[]
		w,h=image.size
		self.sort_name=""

		self.data = [j*h+i for j in range(h) for i in range(w)]
		
		# print(self.data)
		for i in range(w):
			self.pixel_map.append([])
			for j in range(h):
				r,g,b = image.getpixel((i,j))
				self.pixel_map[i].append((r,g,b))
		self.dimensions = (w,h)
		surface = pygame.Surface(self.dimensions)
		self.pixel_array = pygame.PixelArray(surface)
		self.location = location
		self.refresh()
		self.generator=None
		self.sorting=False
		self.speed_multiplier=1
	
	def shuffle_data(self):
		shuffle(self.data)
		self.refresh()

	def sort_data(self):
		self.data = [j*self.dimensions[1]+i for j in range(self.dimensions[1]) for i in range(self.dimensions[0])]
		self.refresh()

	def reverse_data(self):
		self.data = [self.dimensions[0]*self.dimensions[1]-(j*self.dimensions[1]+i)-1 for j in range(self.dimensions[1]) for i in range(self.dimensions[0])]
		self.refresh()

	def refresh(self):
		for i in range(self.dimensions[0]):
			for j in range(self.dimensions[1]):
				self.pixel_array[i][j]=self.pixel_map[self.data[i*self.dimensions[1]+j]//self.dimensions[1]][self.data[i*self.dimensions[1]+j]%self.dimensions[1]]

	def restart_sort(self):
		self.set_sort(self.sort_name)

	def set_sort(self, sort_name):
		self.sort_name=sort_name
		if sort_name == "Stooge Sort":
			self.generator=sortfunctions.stooge_sort(self.data,0,self.dimensions[0]*self.dimensions[1]-1)
			# self.speed_multiplier=self.dimensions[0]
		elif sort_name == "Cycle Sort":
			self.generator=sortfunctions.cycle_sort(self.data)
			self.speed_multiplier=self.dimensions[0]
		elif sort_name == "Cocktail Shaker Sort":
			self.generator=sortfunctions.cocktail_shaker_sort(self.data)
			self.speed_multiplier=self.dimensions[0]*self.dimensions[0]*4
		elif sort_name == "Pancake Sort":
			self.generator=sortfunctions.pancake_sort(self.data)
			self.speed_multiplier=self.dimensions[0]
		elif self.sort_name == "Radix Sort":
			self.generator = sortfunctions.radix_sort(self.data)
			self.speed_multiplier=self.dimensions[0]
		elif self.sort_name == "Bitonic Sort":
			self.generator = sortfunctions.sort_bitonic(self.data)
			self.speed_multiplier=self.dimensions[0]*4
	
	def step(self):
		if self.sorting:
			try:
				# next(self.generator)
				for i in range(self.speed_multiplier):
					next(self.generator)
				self.refresh()
			except StopIteration:
				self.sorting=False
				self.refresh()

	def render(self, screen):
		s=self.pixel_array.make_surface()
		w=s.get_width()
		h=s.get_height()
		
		s=pygame.transform.scale(s, (w*2.5, h*2.5))
		
		s.unlock()
		screen.blit(s, self.location)