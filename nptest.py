import numpy as np
import pygame
import matplotlib.pyplot as plt
from scipy import signal

sampleRate = 44100
freq = 440

pygame.mixer.init(44100,-16,2,512)
# sampling frequency, size, channels, buffer

# Sampling frequency
# Analog audio is recorded by sampling it 44,100 times per second, 
# and then these samples are used to reconstruct the audio signal 
# when playing it back.

# size
# The size argument represents how many bits are used for each 
# audio sample. If the value is negative then signed sample 
# values will be used.

# channels
# 1 = mono, 2 = stereo

# buffer
# The buffer argument controls the number of internal samples 
# used in the sound mixer. It can be lowered to reduce latency, 
# but sound dropout may occur. It can be raised to larger values
# to ensure playback never skips, but it will impose latency on sound playback. 

# arr = np.array([4096 * np.sin(2.0 * np.pi * freq * x / sampleRate) for x in range(0, sampleRate)]).astype(np.int16)
# arr=(4096*np.sin((100/10)*2.0*np.pi*freq*np.arange(0,sampleRate)/sampleRate)).astype(np.int16)
t=np.linspace(0,1,44100)
arr=signal.sawtooth(2*5*np.pi*t,1)

# r=(0,100)
# arr[r[0]:r[1]]=0

# r=(100,200)
# arr[r[0]:r[1]]=arr[r[0]:r[1]]*np.arange(r[1]-r[0])/(r[1]-r[0])

# r=(4210,4310)
# arr[r[0]:r[1]]=arr[r[0]:r[1]]*np.arange(r[1]-r[0],0,-1)/(r[1]-r[0])

# r=(4310,-100)
# arr[r[0]::]=0
maxtime=100
# low=100
# fade=1500

# r=(0,low)
# arr[r[0]:r[1]]=0

# r=(low,fade)
# arr[r[0]:r[1]]=arr[r[0]:r[1]]*np.arange(r[1]-r[0])/(r[1]-r[0])

# r=(int(sampleRate*(maxtime/1000)-fade),int(sampleRate*(maxtime/1000)-low))
# arr[r[0]:r[1]]=arr[r[0]:r[1]]*np.arange(r[1]-r[0],0,-1)/(r[1]-r[0])

# r=(int(sampleRate*(maxtime/1000)-low),0)
# arr[r[0]::]=0

arr2=np.c_[arr,arr]

# sound = pygame.sndarray.make_sound(arr2)
# sound.play(maxtime=100)
# pygame.time.delay(1000)
# sound.stop()

plt.plot(np.arange(sampleRate),arr)
plt.show()