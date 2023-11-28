from constants import *
from scene import Scene
from button import Button
from label import Label

class ChompSorter:
	def __init__(self, scenes):
		self.screen = pygame.display.set_mode(SCREEN_RES)
		pygame.init()
		pygame.display.set_caption("Chomp Sorter")
		self.clock = pygame.time.Clock()
		
		self.scenes = scenes
		self.current_scene = scenes[0]

		self.running = True

	def render(self):
		self.current_scene.render(self.screen)
	
	def loop(self):
		while self.running:
			self.screen.fill(WHITE)

			self.handle_input()

			self.render()

			pygame.display.update()
			self.clock.tick()

	def change_scene(self, scene_tag):
		for scene in self.scenes:
			if scene.tag == scene_tag:
				self.current_scene = scene
				return True
		return False

	def handle_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
			
			if event.type  == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					pass
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				clicked_obj = None
				for obj in self.current_scene.buttons:
					if obj.border_rect.collidepoint(event.pos):
						clicked_obj = obj

def test():
	btns = []
	btns.append(Button("BUTTON", (SCREEN_RES[0]/2, SCREEN_RES[1]/2)))
	btns.append(Button("LARGE BUTTON", (SCREEN_RES[0]/2, 2*SCREEN_RES[1]/3), LRG_BTN_FSIZE))

	lbls = []
	lbls.append(Label("LABEL", (SCREEN_RES[0]/2, SCREEN_RES[1]/3)))
	test_scn = Scene("TEST", btns, lbls)
	return ChompSorter([test_scn])
