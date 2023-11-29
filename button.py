from label import Label
from constants import *

class Button(Label):
	def __init__(self, txt, location, font_size=BTN_FSIZE, bg_color=ORANGE, txt_color=WHITE, bdr_color=WHITE, btn_size=None):
		super().__init__(txt, location, font_size, txt_color)
		if btn_size:
			self.rect = pygame.Rect(self.txt_rect)
			self.rect.width = btn_size[0]
			self.rect.height = btn_size[1]
			self.rect.center = self.txt_rect.center
		else:
			self.rect = self.txt_rect.inflate(BTN_PAD, BTN_PAD)
		self.bg_color = bg_color
		self.bdr_color = bdr_color
		self.txt = txt
		self.border_rect = self.rect.inflate(BTN_BORDER, BTN_BORDER)

	def render(self, screen):
		screen.fill(self.bdr_color, self.border_rect)
		screen.fill(self.bg_color, self.rect)
		super().render(screen)