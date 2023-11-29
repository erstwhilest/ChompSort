from constants import *

class Scene():
	def __init__(self, tag, drawables=[], clickables=[]):
		self.tag = tag
		self.drawables = drawables
		self.clickables = clickables
	
	def render(self, screen):
		for obj in self.drawables+self.clickables:
			obj.render(screen)