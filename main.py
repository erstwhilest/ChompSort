import pygame
import random
import numpy as np

data=[i+1 for i in range(50)]
data_max=max(data)


sampleRate = 44100
freq = 440

pygame.mixer.init(44100,-16,2,512)

sound_arrays=[]
for i in range(len(data)):
	arr=(4096*np.sin((i/10)*2.0*np.pi*freq*np.arange(0,sampleRate)/sampleRate)).astype(np.int16)
	maxtime=40
	low=100
	fade=1500

	r=(0,low)
	arr[r[0]:r[1]]=0

	r=(low,fade)
	arr[r[0]:r[1]]=arr[r[0]:r[1]]*np.arange(r[1]-r[0])/(r[1]-r[0])

	r=(int(sampleRate*(maxtime/1000)-fade),int(sampleRate*(maxtime/1000)-low))
	arr[r[0]:r[1]]=arr[r[0]:r[1]]*np.arange(r[1]-r[0],0,-1)/(r[1]-r[0])

	r=(int(sampleRate*(maxtime/1000)-low),0)
	arr[r[0]::]=0

	arr2=np.c_[arr,arr]
	sound_arrays.append(pygame.sndarray.make_sound(arr2))

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
			sound_arrays[data[j]].play(maxtime=maxtime)
			for k in range(len(data)):
				color=colors[k]
				if k==j+1:
					color="red"
				rects[i]=pygame.Rect(positions[k], SCREEN_SIZE[1]-(data[k]*height), width-1, height*data[k]+1)
				pygame.draw.rect(screen, color, rects[i])
			yield True
	colors[0]="green"
	screen.fill("black")
	for i in range(n):
		screen.fill("black")
		sound_arrays[i].play(maxtime=maxtime)
		for k in range(len(data)):
			color=colors[k]
			if i==k:
				color="red"
			rects[i]=pygame.Rect(positions[k], SCREEN_SIZE[1]-(data[k]*height), width-1, height*data[k]+1)
			pygame.draw.rect(screen, color, rects[i])
		yield True
	
generator = bubble_sort(data, screen)

sorting=False

speed=2

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key==pygame.K_RETURN:
				sorting=True

	last_time=time
	time=pygame.time.get_ticks()

	if last_time // speed != time // speed:
		if sorting:
			try:
				next(generator)
			except StopIteration:
				sorting=False

	pygame.display.flip()

	clock.tick(-1)

pygame.quit()