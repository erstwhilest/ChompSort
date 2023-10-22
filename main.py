import pygame
import random

data=[i for i in range(1,100)]

pygame.init()
SCREEN_SIZE = (1920, 1080)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

last_time=0
time=0

height=SCREEN_SIZE[1]/max(data)

random.shuffle(data)

start_offset=0
width=SCREEN_SIZE[0]/len(data)

colors=[]
for i in range(len(data)):
	colors.append("white")

sort="bubble"

positions=[]
rects=[]
for i in range(len(data)):
	positions.append(start_offset+i*width)
	rects.append(pygame.Rect(positions[i], SCREEN_SIZE[1]-(data[i]*height), width-1, height*data[i]+1))

def bubble_sort(arr, screen):
	n = len(arr)
	
	for i in range(n):
		if i!=0:
			colors[n-i]="green"
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				screen.fill("black")
				for k in range(len(data)):
					color=colors[k]
					if k==j+1:
						color="red"
					rects[i]=pygame.Rect(positions[k], SCREEN_SIZE[1]-(data[k]*height), width-1, height*data[k]+1)
					pygame.draw.rect(screen, color, rects[i])
				yield True
			else:
				screen.fill("black")
				for k in range(len(data)):
					color=colors[k]
					if k==j+1:
						color="red"
					rects[i]=pygame.Rect(positions[k], SCREEN_SIZE[1]-(data[k]*height), width-1, height*data[k]+1)
					pygame.draw.rect(screen, color, rects[i])
				yield True
	
generator = bubble_sort(data, screen)

sorting=False

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_RETURN:
				sorting=True

	last_time=time
	time=pygame.time.get_ticks()

	if  last_time//1 != time//1:
		if sorting:
			try:
				next(generator)
			except StopIteration:
				sorting=False

	pygame.display.flip()

	clock.tick(144)

pygame.quit()