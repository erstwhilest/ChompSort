from constants import *
from scene import Scene
from button import Button
from label import Label
from soundmanager import SoundManager
from datavisualizer import DataVisualizer
from slider import Slider
from pixelarray import PixelArray

class ChompSorter:
	def __init__(self, scenes, data_visualizer, pixel_array):
		self.screen = pygame.display.set_mode(SCREEN_RES)
		pygame.init()
		pygame.display.set_caption("Chomp Sorter")
		img=pygame.image.load("CHOMPSORT_ICON_2.jpeg")
		pygame.display.set_icon(img)

		self.clock = pygame.time.Clock()
		
		self.scenes = scenes
		self.current_scene = scenes[0]

		self.data_visualizer=data_visualizer
		self.pixel_array=pixel_array

		self.running = True

		self.period = 100 # in ms

		self.time=0
		self.last_time=0

		self.held_obj = None

		self.static_text = [
			["Radix Sort",
			 "Radix sort is a non-comparative sorting algorithm that",
			 "sorts integers by processing individual digits, from",
			 "the least significant to the most significant, using",
			 "counting or bucket sort at each digit position.",
			 "",
			 "Time Complexity: O(nd)",
			 "n - number of digits, d - size of largest number"],

			["Bitonic Sort",
			 "Bitonic sort recursively constructs bitonic sequences,",
			 "merges adjacent sequences in a bitonic manner, and",
			 " performs a final bitonic merge to achieve sorting.",
			 "",
			 "Time Complexity: O(log^2(n))",
			 "n - number of elements to be sorted",
			 ""],

			["Pancake Sort",
			 "Pancake sort is a inefficient sort that works by",
			 "repeatedly flipping the elements in the array prefix.",
			 "It finds the largest unsorted element and flips the",
			 "subarray to bring the largest element to the end.",
			 "",
			 "Time Complexity: O(n^2)",
			 "n - number of elements to be sorted"],

			["Cocktail Shaker Sort",
			 "Basically a bi-directional bubble sort algorithm.",
			 "It works by  traversing the array in both directions,",
			 "comparing adjacent elements, bubbling large elements",
			 "to the end, and then the smallest to the beginning.",
			 "",
			 "Time Complexity: O(n^2)",
			 "n - number of elements to be sorted"],

			["Stooge Sort",
			 "It divides the array into three parts and recursively",
			 "sorts the first 2/3 and last 2/3 of the array. This",
			 "process continues until the the entire array is sorted",
			 "by recursively sorting the first two-thirds again.",
			 "",
			 "Time Complexity: O(n^(log3/log1.5)",
			 "n - number of elements to be sorted"],

			["Cycle Sort",
			 "The basic idea behind cycle sort is to divide the input",
			 "array into cycles, where each cycle consists of elements",
			 "that belong to the same position in the sorted array.",
			 "The algorithm then swaps each element in its cycle",
			 "",
			 "Time Complexity: O(n^2)",
			 "n - number of elements to be sorted"]
		]

	def render(self):
		self.current_scene.render(self.screen)
	
	def loop(self):
		count = 0
		while self.running:
			self.screen.fill(BLACK)

			self.handle_input()

			self.last_time=self.time
			self.time=pygame.time.get_ticks()

			if self.last_time // self.period != self.time // self.period:
				self.data_visualizer.step()
				self.pixel_array.step()
				if self.data_visualizer.complete is True:
					self.data_visualizer.sorted(count)
					count += 1
				else:
					count = 0

			self.screen.fill(BLACK)
			self.render()
			pygame.display.update()
			self.clock.tick(144)

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

			if self.data_visualizer.data_count_backround != self.data_visualizer.data_count:
				self.scenes[1].drawables[0].change_text("Note: Max Visualization 512")
			else:
				self.scenes[1].drawables[0].change_text(" ")


			if event.type  == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					pass
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				clicked_obj = None
				for obj in self.current_scene.clickables:
					if type(obj) == Button and obj.border_rect.collidepoint(event.pos):
						clicked_obj = obj
					elif type(obj) == Slider and (obj.track_rect.collidepoint(event.pos) or obj.thumb_rect.collidepoint(event.pos)):
						clicked_obj = obj
				if type(clicked_obj) == Button:
					if clicked_obj.tag in SORT_NAMES:
						self.change_scene("GRAPH")
						self.data_visualizer.set_sort(clicked_obj.tag)
						self.pixel_array.set_sort(clicked_obj.tag)

					if clicked_obj.tag == "Menu":
						self.data_visualizer.sorting=False
						self.pixel_array.sorting=False
						self.data_visualizer.restart_sort()
						self.data_visualizer.sort_data()
						self.pixel_array.restart_sort()
						self.pixel_array.sort_data()
						self.change_scene("MENU")

					if clicked_obj.tag == "Settings":
						self.change_scene("SETTINGS")

					if clicked_obj.tag == " Sorted ":
						self.data_visualizer.restart_sort()
						self.data_visualizer.sort_data()
						self.pixel_array.restart_sort()
						self.pixel_array.sort_data()

					if clicked_obj.tag == "Shuffled":
						self.data_visualizer.sorting=False
						self.pixel_array.sorting=False
						self.data_visualizer.restart_sort()
						self.data_visualizer.shuffle_data()
						self.pixel_array.restart_sort()
						self.pixel_array.shuffle_data()

					if clicked_obj.tag == "Reversed":
						self.data_visualizer.sorting=False
						self.pixel_array.sorting=False
						self.data_visualizer.restart_sort()
						self.data_visualizer.reverse_data()
						self.pixel_array.restart_sort()
						self.pixel_array.reverse_data()

					if clicked_obj.tag == "Start":
						self.data_visualizer.restart_sort()
						self.pixel_array.restart_sort()
						self.data_visualizer.sorting=True
						self.pixel_array.sorting=True

					if clicked_obj.tag == "Info":
						self.change_scene("INFO")
						if self.data_visualizer.sort_name == "Radix Sort":
							for index, item in enumerate(self.scenes[3].drawables):
								item.change_text(self.static_text[0][index])
						elif self.data_visualizer.sort_name == "Bitonic Sort":
							for index, item in enumerate(self.scenes[3].drawables):
								item.change_text(self.static_text[1][index])
						elif self.data_visualizer.sort_name == "Pancake Sort":
							for index, item in enumerate(self.scenes[3].drawables):
								item.change_text(self.static_text[2][index])
						elif self.data_visualizer.sort_name == "Cocktail Shaker Sort":
							for index, item in enumerate(self.scenes[3].drawables):
								item.change_text(self.static_text[3][index])
						elif self.data_visualizer.sort_name == "Stooge Sort":
							for index, item in enumerate(self.scenes[3].drawables):
								item.change_text(self.static_text[4][index])
						elif self.data_visualizer.sort_name == "Cycle Sort":
							for index, item in enumerate(self.scenes[3].drawables):
								item.change_text(self.static_text[5][index])

					if clicked_obj.tag == "exit":
						self.change_scene("GRAPH")


				if type(clicked_obj) == Slider:
					self.held_obj = clicked_obj
			
			if event.type == pygame.MOUSEBUTTONUP:
				self.held_obj = None

		if self.held_obj != None:
			if self.held_obj.tag == "Speed":
				self.period = self.held_obj.move(pygame.mouse.get_pos())
			if self.held_obj.tag == "Data Size":
				self.data_visualizer.resize(int(self.held_obj.move(pygame.mouse.get_pos())))
			if self.held_obj.tag == "Sound Type":
				self.data_visualizer.sound_manager.select_sound(self.held_obj.tagset[self.held_obj.move(pygame.mouse.get_pos())])
				
						

def populate():
	sort_layout=[["Radix Sort", "Bitonic Sort", "Pancake Sort"], ["Cocktail Shaker Sort", "Stooge Sort", "Cycle Sort"]]

	btns = []
	for i in range(len(sort_layout)):
		for j in range(len(sort_layout[i])):
			btns.append(Button(sort_layout[i][j], (SCREEN_RES[0]*(j+1)/(len(sort_layout[i])+1), SCREEN_RES[1]/2+SCREEN_RES[1]/2*(i+1)/(len(sort_layout)+1)), btn_size=(SCREEN_RES[0]/5, SCREEN_RES[1]/10)))
	btns.append(Button("Settings", (SCREEN_RES[0]-YPAD*2-BTN_PAD, SCREEN_RES[1]-YPAD-BTN_PAD)))

	draw = []
	draw.append(Label("Chomp Sorter", (SCREEN_RES[0]/2, SCREEN_RES[1]/4)))
	draw.append(Label("Select a sort to begin!", (SCREEN_RES[0]/2, SCREEN_RES[1]*2/4), SML_LBL_FSIZE))

	menu_scene = Scene("MENU", draw, btns)

	click = []
	click.append(Button("Menu", (SCREEN_RES[0]*4/8, YPAD*3)))
	click.append(Button("Info", (SCREEN_RES[0] * 4 / 8, YPAD*5)))
	click.append(Button(" Sorted ", (SCREEN_RES[0]*3/8, YPAD*1)))
	click.append(Button("Shuffled", (SCREEN_RES[0]*3/8, YPAD*3)))
	click.append(Button("Reversed", (SCREEN_RES[0]*3/8, YPAD*5)))
	click.append(Button("Start", (SCREEN_RES[0]*2/8, YPAD*1)))
	click.append(Slider("Speed", (SCREEN_RES[0]*5/8, YPAD*2), SCREEN_RES[0]/4, 1, 1000, suffix=" ms (between steps)", reversed=True))
	period=click[-1].value
	click.append(Slider("Data Size", (SCREEN_RES[0]*5/8, YPAD*3+THUMB_SIZE[1]), SCREEN_RES[0]/4, 2, 131072, pow2=True))
	data_size=click[-1].value

	draw = []
	data=DataVisualizer(data_size, pygame.Rect(YPAD*2, YPAD*6, SCREEN_RES[0]-YPAD*4, SCREEN_RES[1]-(YPAD*6)), SoundManager())
	pixel=PixelArray("gator64.jpg", (YPAD*2,0))
	draw.append(Label("", (SCREEN_RES[0] / 2 + 325, SCREEN_RES[1] / 4 - 16), BTN_FSIZE))
	draw.append(data)
	draw.append(pixel)
	
	graph_scene = Scene("GRAPH", draw, click)


	click=[]
	click.append(Slider("Sound Type", (SCREEN_RES[0]/16, SCREEN_RES[1]/8), SCREEN_RES[0]/6, 0, 1, tagset=["Triangle", "Sine"]))
	click.append(Button("Menu", (SCREEN_RES[0]-YPAD*2, YPAD)))
	draw=[]
	settings_scene = Scene("SETTINGS", draw, click)

	info_btns = []
	info_btns.append(Button("", (SCREEN_RES[0]/2, SCREEN_RES[1]/2), btn_size=(SCREEN_RES[0]/1.2, SCREEN_RES[1]/1.5)))
	info_btns.append(Button("exit", (SCREEN_RES[0] - YPAD * 2 - BTN_PAD, SCREEN_RES[1] - YPAD - BTN_PAD)))

	draw = []
	draw.append(Label("", (SCREEN_RES[0] / 2, SCREEN_RES[1] / 4)))
	draw.append(Label("", (SCREEN_RES[0] / 2, SCREEN_RES[1] * 2 / 4 - 2 * INFO_LBL_FSIZE * 1.3), INFO_LBL_FSIZE))
	draw.append(Label("", (SCREEN_RES[0] / 2, SCREEN_RES[1] * 2 / 4 - INFO_LBL_FSIZE * 1.3), INFO_LBL_FSIZE))
	draw.append(Label("", (SCREEN_RES[0] / 2, SCREEN_RES[1] * 2 / 4), INFO_LBL_FSIZE))
	draw.append(Label("", (SCREEN_RES[0] / 2, SCREEN_RES[1] * 2 / 4 + INFO_LBL_FSIZE * 1.3), INFO_LBL_FSIZE))
	draw.append(Label("", (SCREEN_RES[0] / 2, SCREEN_RES[1] * 2 / 4 + 2 * INFO_LBL_FSIZE * 1.3), INFO_LBL_FSIZE))
	draw.append(Label("", (SCREEN_RES[0] / 2, SCREEN_RES[1] * 2 / 4 + 3 * INFO_LBL_FSIZE * 1.3), INFO_LBL_FSIZE))
	draw.append(Label("", (SCREEN_RES[0] / 2, SCREEN_RES[1] * 2 / 4 + 4 * INFO_LBL_FSIZE * 1.3), INFO_LBL_FSIZE))

	#rects = []
	#rects.append(pygame.Rect(100, 50, 200, 100))

	info_scene = Scene("INFO", draw, info_btns)

	cs=ChompSorter([menu_scene, graph_scene, settings_scene, info_scene], data, pixel)
	cs.period=period
	return cs
