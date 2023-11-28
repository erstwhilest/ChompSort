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
				if type(clicked_obj) == Button:
					if clicked_obj.tag in SORT_NAMES:
						self.change_scene("GRAPH")
					if clicked_obj.tag == "Menu":
						self.change_scene("MENU")

def populate():
	sort_layout=[["Radix Sort", "Bitonic Sort", "Pancake Sort"], ["Cocktail Shaker Sort", "Stooge Sort", "Cycle Sort"]]

	btns = []
	for i in range(len(sort_layout)):
		for j in range(len(sort_layout[i])):
			btns.append(Button(sort_layout[i][j], (SCREEN_RES[0]*(j+1)/(len(sort_layout[i])+1), SCREEN_RES[1]/2+SCREEN_RES[1]/2*(i+1)/(len(sort_layout)+1)), btn_size=(SCREEN_RES[0]/5, SCREEN_RES[1]/10)))

	lbls = []
	lbls.append(Label("Chomp Sorter", (SCREEN_RES[0]/2, SCREEN_RES[1]/4)))
	lbls.append(Label("Select a sort to begin!", (SCREEN_RES[0]/2, SCREEN_RES[1]*2/4), SML_LBL_FSIZE))

	menu_scene = Scene("MENU", btns, lbls)

	btns = []
	btns.append(Button("Menu", (SCREEN_RES[0]/2, 50)))
	lbls = []
	graph_scene = Scene("GRAPH", btns, lbls)

	return ChompSorter([menu_scene, graph_scene])
