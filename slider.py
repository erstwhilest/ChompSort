from constants import *
from label import Label
import math

class Slider(Label):
	def __init__(self, tag, location, width, slider_min, slider_max, font_size=BTN_FSIZE, suffix="", tagset=[], reversed=False, pow2=False):
		self.thumb_rect = pygame.Rect((location[0]+width/2-THUMB_SIZE[0]/2, location[1]), THUMB_SIZE)
		self.track_rect = pygame.Rect((location[0], location[1]+THUMB_SIZE[1]/2-TRACK_HEIGHT/2), (width, TRACK_HEIGHT))
		self.percentage = 0
		self.min = slider_min
		self.max = slider_max
		self.suffix=suffix
		self.tagset=tagset
		self.reversed=reversed
		self.pow2=pow2
		if self.pow2:
			self.value=2**round((.5*(int(math.log2(self.max)-int(math.log2(self.min))))+int(math.log2(self.min))))
		else:
			self.value = round(slider_max/2)
		super().__init__(tag, (self.track_rect.x+self.track_rect.w/2, location[1]-THUMB_SIZE[1]/2), font_size, WHITE)
		if tagset != []:
			self.change_text(self.tag+": "+tagset[self.value]+suffix)
		else:
			self.change_text(self.tag+": "+str(self.value)+suffix)

	def get_tag_selection(self):
		if self.tagset==[]:
			return None
		else:
			return self.tagset[self.value]

	def render(self, screen):
		screen.fill(WHITE, self.track_rect)
		screen.fill(ORANGE, self.thumb_rect)
		super().render(screen)
	
	def move(self, mouse_pos):
		# follow mouse, change value
		if mouse_pos[0]<self.track_rect.x:
			self.thumb_rect[0]=self.track_rect.x
		elif mouse_pos[0]>self.track_rect.x+self.track_rect.w:
			self.thumb_rect.x=self.track_rect.x+self.track_rect.w-THUMB_SIZE[0]/2
		else:
			self.thumb_rect.x=mouse_pos[0]-THUMB_SIZE[0]/2

		if self.reversed:
			self.percentage=1-max(min(((mouse_pos[0]-self.track_rect.x)/self.track_rect.w), 1), 0)
		else:
			self.percentage=max(min(((mouse_pos[0]-self.track_rect.x)/self.track_rect.w), 1), 0)

		if self.pow2:
			self.value = 2**round((self.percentage*(int(math.log2(self.max)-int(math.log2(self.min))))+int(math.log2(self.min))))
			# print(2**round((self.percentage*(int(math.log2(self.max)-int(math.log2(self.min))))+int(math.log2(self.min)))))
			# print(2**int(math.log2(self.min)))
		else:
			self.value = round((self.max-self.min)*self.percentage+self.min)

		if self.tagset != []:
			self.change_text(self.tag+": "+self.tagset[round(self.percentage*(len(self.tagset)-1))]+self.suffix)
		else:
			self.change_text(self.tag+": "+str(self.value)+self.suffix)
		return self.value