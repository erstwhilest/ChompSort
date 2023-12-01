from constants import *
from scene import Scene
from button import Button
from label import Label
from soundmanager import SoundManager
from datavisualizer import DataVisualizer

class ChompSorter:
	def __init__(self, scenes, data_visualizer):
		self.screen = pygame.display.set_mode(SCREEN_RES)
		pygame.init()
		pygame.display.set_caption("Chomp Sorter")
		pygame.display.set_icon(pygame.image.load('CHOMPSORT_ICON_2.jpeg'))
		self.clock = pygame.time.Clock()
		
		self.scenes = scenes
		self.current_scene = scenes[0]

		self.data_visualizer = data_visualizer

		self.running = True

		self.period = 100 # in ms

		self.time=0
		self.last_time=0

	def render(self):
		self.current_scene.render(self.screen)

	def loop(self):
		while self.running:
			self.screen.fill(BLACK)

			self.handle_input()

			self.last_time=self.time
			self.time=pygame.time.get_ticks()

			if self.last_time // self.period != self.time // self.period:
				self.data_visualizer.step()

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
				for obj in self.current_scene.clickables:
					if obj.border_rect.collidepoint(event.pos):
						clicked_obj = obj
				if type(clicked_obj) == Button:
					if clicked_obj.tag in SORT_NAMES:
						self.change_scene("GRAPH")
						self.data_visualizer.set_sort(clicked_obj.tag)
					if clicked_obj.tag == "Menu":
						self.change_scene("MENU")
					if clicked_obj.tag == "Shuffle":
						self.data_visualizer.shuffle_data()
					if clicked_obj.tag == "Start":
						self.data_visualizer.sorting=True

					if clicked_obj.tag == "Stop":
						self.data_visualizer.sorting=False

def populate():
	sort_layout=[["Radix Sort", "Bitonic Sort", "Pancake Sort"], ["Cocktail Shaker Sort", "Stooge Sort", "Cycle Sort"]]

	btns = []
	for i in range(len(sort_layout)):
		for j in range(len(sort_layout[i])):
			btns.append(Button(sort_layout[i][j], (SCREEN_RES[0]*(j+1)/(len(sort_layout[i])+1), SCREEN_RES[1]/2+SCREEN_RES[1]/2*(i+1)/(len(sort_layout)+1)), btn_size=(SCREEN_RES[0]/5, SCREEN_RES[1]/10)))

	draw = []
	draw.append(Label("Chomp Sorter", (SCREEN_RES[0]/2, SCREEN_RES[1]/4)))
	draw.append(Label("Select a sort to begin!", (SCREEN_RES[0]/2, SCREEN_RES[1]*2/4), SML_LBL_FSIZE))

	menu_scene = Scene("MENU", draw, btns)

	click = []
	click.append(Button("Menu", (SCREEN_RES[0]*4/8, YPAD)))
	click.append(Button("Shuffle", (SCREEN_RES[0]*3/8, YPAD)))
	click.append(Button("Start", (SCREEN_RES[0]*1/8, YPAD)))
	click.append(Button("Stop", (SCREEN_RES[0]*2/8, YPAD)))
	draw = []
	data=DataVisualizer(10, pygame.Rect(YPAD*2, YPAD*2, SCREEN_RES[0]-YPAD*4, SCREEN_RES[1]))
	draw.append(data)
	graph_scene = Scene("GRAPH", draw, click)

	return ChompSorter([menu_scene, graph_scene], data)
