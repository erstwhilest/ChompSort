from constants import *

class Label():
	def __init__(self, txt, location, font_size=LBL_FSIZE, color=WHITE):
		self.font = pygame.font.Font(FONT, font_size)
		self.rendered_text = self.font.render(txt, True, color)
		self.txt_rect = self.rendered_text.get_rect(center=location)
		self.tag = txt
		self.color= color
		self.location=location
	
	def change_text(self, new_text):
		self.rendered_text=self.font.render(new_text,True,self.color)
		self.txt_rect=self.rendered_text.get_rect(center=self.location)

	def render(self, screen):
		screen.blit(self.rendered_text, self.txt_rect)