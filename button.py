from label import Label
from constants import *

class Button(Label):
	def __init__(self, txt, location, font_size=BTN_FSIZE, bg_color=ORANGE, txt_color=BLACK, bdr_color=BLACK):
		super().__init__(txt, location, font_size, txt_color)
		self.rect = self.txt_rect.inflate(BTN_PAD, BTN_PAD)
		self.bg_color = bg_color
		self.bdr_color = bdr_color
		self.txt = txt
		self.border_rect = self.rect.inflate(BTN_BORDER, BTN_BORDER)

	def render(self, screen):
		screen.fill(self.bdr_color, self.border_rect)
		screen.fill(self.bg_color, self.rect)
		super().render(screen)