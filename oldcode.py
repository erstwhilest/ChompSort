import pygame
import random
import numpy as np
from scipy import signal

count=25
# data=[random.randint(1,count) for i in range(count)]
data=[i+1 for i in range(count)]
data_max=max(data)

sorted_data=[i for i in data]
random.shuffle(data)
# data.reverse()

sampleRate = 44100
freq = 440

pygame.mixer.init(44100,-16,2,512)

sound_arrays=[]
frequency_count=50
for i in range(frequency_count+1):
	# arr=(4096*np.sin((i/10)*2.0*np.pi*freq*np.arange(0,sampleRate)/sampleRate)).astype(np.int16) # sine wave
	arr=(4096*signal.sawtooth((i/frequency_count*3)*2*np.pi*freq*np.arange(0,sampleRate)/sampleRate,.5)).astype(np.int16) # triangle wave
	# arr=(4096*signal.sawtooth((i/10)*2*np.pi*freq*np.arange(0,sampleRate)/sampleRate,0)).astype(np.int16) # sawtooth wave
	# arr=(4096*signal.sawtooth((i/10)*2*np.pi*freq*np.arange(0,sampleRate)/sampleRate,1)).astype(np.int16) # reversed sawtooth wave
	maxtime=70
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
# SCREEN_SIZE = (2560, 1440)
SCREEN_SIZE = (1920, 1080)
# SCREEN_SIZE = (1280, 720)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True

last_time=0
time=0

height=SCREEN_SIZE[1]/max(data)

start_offset=0
width=SCREEN_SIZE[0]/len(data)

colors=[]
for i in range(len(data)):
	colors.append("white")

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
			sound_arrays[int(data[j]/data_max*frequency_count)].play(maxtime=maxtime)
			for k in range(len(data)):
				color=colors[k]
				if k==j+1:
					color="red"
				rects[i]=pygame.Rect(positions[k], SCREEN_SIZE[1]-(data[k]*height), width-1, height*data[k]+1)
				pygame.draw.rect(screen, color, rects[i])
			yield True
	colors[0]="green"
	for i in range(n):
		screen.fill("black")
		sound_arrays[int(data[i]/data_max*frequency_count)].play(maxtime=maxtime)
		for k in range(len(data)):
			color=colors[k]
			if i==k:
				color="red"
			rects[i]=pygame.Rect(positions[k], SCREEN_SIZE[1]-(data[k]*height), width-1, height*data[k]+1)
			pygame.draw.rect(screen, color, rects[i])
		yield True

def stooge_sort_draw(l,h):
	screen.fill("black")
	color="white"
	sound_arrays[int(data[l]/data_max*frequency_count)].play(maxtime=maxtime)
	sound_arrays[int(data[h]/data_max*frequency_count)].play(maxtime=maxtime)
	for i in range(len(data)):
		if i==h or i==l:
			color="red"
		elif i<h and i>l:
			color="green"
		else:
			color="white"
		rects[i]=pygame.Rect(positions[i], SCREEN_SIZE[1]-(data[i]*height), width+1, height*data[i]+1)
		pygame.draw.rect(screen, color, rects[i])

def stooge_sort(arr, l, h, screen):

	# PLACE HERE TO SHOW ALL ITERATIONS
	# must also add yield True to end
	stooge_sort_draw(l,h)
	
	if l >= h:
		return
	if arr[l]>arr[h]:
		arr[l],arr[h]=arr[h],arr[l]

		# PLACE HERE TO SHOW SWAPS
		# stooge_sort_draw(l,h)
		# yield True

	if h-l+1>2:
		temp=int((h-l+1)/3)
		yield from stooge_sort(arr,l,h-temp,screen)
		yield from stooge_sort(arr,l+temp,h,screen)
		yield from stooge_sort(arr,l,h-temp,screen)
	yield True
	
def cycle_sort_draw(item, i):
	screen.fill("black")
	sound_arrays[int(data[i]/data_max*frequency_count)].play(maxtime=maxtime)
	for k in range(len(data)):
		color=colors[k]
		if k==i or k==item-1:
			color="red"
		rects[k]=pygame.Rect(positions[k], SCREEN_SIZE[1]-(data[k]*height), width+1, height*data[k]+1)
		pygame.draw.rect(screen, color, rects[k])

def cycle_sort(array) -> int:
	"""Sort an array in place and return the number of writes."""
	writes = 0

	# Loop through the array to find cycles to rotate.
	# Note that the last item will already be sorted after the first n-1 cycles.
	for cycle_start in range(0, len(array) - 1):
		item = array[cycle_start]

		# Find where to put the item.
		pos = cycle_start
		for i in range(cycle_start + 1, len(array)):
			if array[i] < item:
				cycle_sort_draw(item, i)
				yield True
				pos += 1

		if pos == cycle_start:
			continue

		while item == array[pos]:
			pos += 1

		array[pos], item = item, array[pos]
		writes += 1

		cycle_sort_draw(cycle_start, pos)
		colors[pos]="green"
		yield True

		# Rotate the rest of the cycle.
		while pos != cycle_start:
			# Find where to put the item.
			pos = cycle_start
			for i in range(cycle_start + 1, len(array)):
				if array[i] < item:
					cycle_sort_draw(item, i)
					yield True
					pos += 1

			# Put the item there or right after any duplicates.
			while item == array[pos]:
				pos += 1
			array[pos], item = item, array[pos]
			writes += 1

			cycle_sort_draw(item, pos)
			colors[pos]="green"
			yield True

	return writes
	
# generator = bubble_sort(data, screen)
generator=stooge_sort(data,0,len(data)-1,screen)
# generator=cycle_sort(data)

sorting=False

# if sorting:
# 	while data!=sorted_data:
# 		try:
# 			next(generator)
# 			for i in data:
# 				print(i,end=' ')
# 			print()
# 		except StopIteration:
# 			sorting=False

speed=100

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

	clock.tick()

pygame.quit()