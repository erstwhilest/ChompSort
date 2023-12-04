from constants import *

class Scene():
	def __init__(self, tag, drawables=[], clickables=[], rects=[]):
		self.tag = tag
		self.drawables = drawables
		self.clickables = clickables
		self.rects = rects
	
	def render(self, screen):
		for obj in self.rects:
			pygame.draw.rect(screen, ORANGE, obj)

		for obj in self.clickables + self.drawables:
			obj.render(screen)
