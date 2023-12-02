from constants import *
from label import Label

class Slider(Label):
	def __init__(self, tag, location, width, slider_min, slider_max, font_size=BTN_FSIZE, suffix="", tagset=[], reversed=False):
		self.thumb_rect = pygame.Rect((location[0]+width/2-THUMB_SIZE[0]/2, location[1]), THUMB_SIZE)
		self.track_rect = pygame.Rect((location[0], location[1]+THUMB_SIZE[1]/2-TRACK_HEIGHT/2), (width, TRACK_HEIGHT))
		self.value = int(slider_max/2)
		self.percentage = 0
		self.min = slider_min
		self.max = slider_max
		super().__init__(tag, (self.track_rect.x+self.track_rect.w/2, location[1]-THUMB_SIZE[1]/2), font_size, WHITE)
		if tagset != []:
			self.change_text(self.tag+": "+tagset[self.value]+suffix)
		else:
			self.change_text(self.tag+": "+str(self.value)+suffix)
		self.suffix=suffix
		self.tagset=tagset
		self.reversed=reversed

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
		self.value = round((self.max-self.min)*self.percentage+self.min)
		if self.tagset != []:
			self.change_text(self.tag+": "+self.tagset[self.value]+self.suffix)
		else:
			self.change_text(self.tag+": "+str(self.value)+self.suffix)
		return self.value